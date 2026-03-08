#!/usr/bin/env python3
"""GitHub Actions TUI — browse workflow runs, jobs, and logs.

Dependencies:
    pip install textual

Requires:
    - gh CLI (https://cli.github.com/) installed and authenticated
    - Run from within a git repository with a GitHub remote
"""

import json
import subprocess
from datetime import datetime, timezone

from textual.app import App, ComposeWidget
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Header, Static, RichLog
from textual.screen import Screen


# ── Data layer ──────────────────────────────────────────────────────


def _run_gh(*args: str) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def get_repo_name() -> str:
    data = json.loads(_run_gh("repo", "view", "--json", "nameWithOwner"))
    return data["nameWithOwner"]


def gh_run_list(limit: int = 20) -> list[dict]:
    fields = "databaseId,displayTitle,headBranch,status,conclusion,createdAt,workflowName"
    raw = _run_gh("run", "list", "--json", fields, "--limit", str(limit))
    return json.loads(raw)


def gh_run_jobs(run_id: int) -> list[dict]:
    raw = _run_gh("run", "view", str(run_id), "--json", "jobs")
    data = json.loads(raw)
    return data.get("jobs", [])


def gh_job_log(run_id: int) -> str:
    return _run_gh("run", "view", str(run_id), "--log")


# ── Helpers ─────────────────────────────────────────────────────────

STATUS_ICONS = {
    "completed": {"success": "✓", "failure": "✗", "cancelled": "⊘", "skipped": "⊘"},
    "in_progress": "●",
    "queued": "○",
    "waiting": "○",
    "requested": "○",
    "pending": "○",
}


def status_icon(status: str, conclusion: str | None = None) -> str:
    val = STATUS_ICONS.get(status, "?")
    if isinstance(val, dict):
        return val.get(conclusion or "", "?")
    return val


def relative_time(iso_str: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        diff = datetime.now(timezone.utc) - dt
        secs = int(diff.total_seconds())
        if secs < 60:
            return "now"
        if secs < 3600:
            return f"{secs // 60}m"
        if secs < 86400:
            return f"{secs // 3600}h"
        return f"{secs // 86400}d"
    except (ValueError, TypeError):
        return "?"


def format_duration(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "-"
    m, s = divmod(int(seconds), 60)
    return f"{m}m {s:02d}s"


def job_duration(job: dict) -> str:
    started = job.get("startedAt")
    completed = job.get("completedAt")
    if not started:
        return "-"
    try:
        t_start = datetime.fromisoformat(started.replace("Z", "+00:00"))
        if completed:
            t_end = datetime.fromisoformat(completed.replace("Z", "+00:00"))
        else:
            t_end = datetime.now(timezone.utc)
        return format_duration((t_end - t_start).total_seconds())
    except (ValueError, TypeError):
        return "-"


# ── Log parsing ─────────────────────────────────────────────────────


def parse_log_steps(raw_log: str) -> list[dict]:
    """Parse gh run view --log output into steps.

    Lines look like: <job-name>\t<step-name>\t<timestamp> <message>
    """
    steps: dict[str, list[str]] = {}
    step_order: list[str] = []
    for line in raw_log.splitlines():
        parts = line.split("\t", 2)
        if len(parts) < 2:
            continue
        step_name = parts[1] if len(parts) >= 2 else "unknown"
        log_line = parts[2] if len(parts) >= 3 else ""
        if step_name not in steps:
            steps[step_name] = []
            step_order.append(step_name)
        steps[step_name].append(log_line)
    return [{"name": name, "lines": steps[name]} for name in step_order]


# ── Screens / Widgets ──────────────────────────────────────────────


class LogScreen(Screen):
    """Full-screen log viewer with collapsible steps."""

    BINDINGS = [
        Binding("escape", "pop_screen", "Back"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self, run_id: int, job_name: str) -> None:
        super().__init__()
        self.run_id = run_id
        self.job_name = job_name

    def compose(self) -> ComposeWidget:
        yield Header()
        yield RichLog(id="log-view", highlight=True, markup=True)
        yield Footer()

    def on_mount(self) -> None:
        self.title = f"Job: {self.job_name} (#{self.run_id})"
        log_widget = self.query_one("#log-view", RichLog)
        try:
            raw = gh_job_log(self.run_id)
            steps = parse_log_steps(raw)
            if not steps:
                log_widget.write("[dim]No log output[/dim]")
                return
            for step in steps:
                log_widget.write(f"\n[bold]▼ {step['name']}[/bold]")
                for line in step["lines"]:
                    log_widget.write(f"  {line}")
        except RuntimeError as e:
            log_widget.write(f"[red]Error loading log: {e}[/red]")

    def action_pop_screen(self) -> None:
        self.app.pop_screen()


class GHActionsApp(App):
    """GitHub Actions TUI — browse runs, jobs, and logs."""

    CSS = """
    #main-container {
        height: 1fr;
    }
    #runs-pane {
        width: 1fr;
        border-right: solid $primary;
    }
    #jobs-pane {
        width: 1fr;
    }
    .pane-title {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        text-align: center;
        text-style: bold;
    }
    #runs-table, #jobs-table {
        height: 1fr;
    }
    #jobs-header {
        dock: top;
        height: 1;
        background: $surface;
        color: $text-muted;
        padding: 0 1;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("escape", "focus_runs", "Back to Runs"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self._runs: list[dict] = []
        self._jobs: list[dict] = []
        self._selected_run_id: int | None = None

    def compose(self) -> ComposeWidget:
        yield Header()
        with Horizontal(id="main-container"):
            with Vertical(id="runs-pane"):
                yield Static("Runs", classes="pane-title")
                yield DataTable(id="runs-table", cursor_type="row")
            with Vertical(id="jobs-pane"):
                yield Static("", id="jobs-header")
                yield DataTable(id="jobs-table", cursor_type="row")
        yield Footer()

    def on_mount(self) -> None:
        try:
            repo = get_repo_name()
            self.title = f"gh-actions — {repo}"
        except RuntimeError:
            self.title = "gh-actions"

        runs_table = self.query_one("#runs-table", DataTable)
        runs_table.add_columns(" ", "Workflow", "Branch", "Time")

        jobs_table = self.query_one("#jobs-table", DataTable)
        jobs_table.add_columns(" ", "Job", "Duration")

        self._load_runs()
        runs_table.focus()

    def _load_runs(self) -> None:
        runs_table = self.query_one("#runs-table", DataTable)
        runs_table.clear()
        try:
            self._runs = gh_run_list()
        except RuntimeError as e:
            self.notify(f"Error: {e}", severity="error")
            return
        for run in self._runs:
            icon = status_icon(run.get("status", ""), run.get("conclusion"))
            runs_table.add_row(
                icon,
                run.get("workflowName", "")[:20],
                run.get("headBranch", "")[:15],
                relative_time(run.get("createdAt", "")),
                key=str(run["databaseId"]),
            )
        if self._runs:
            self._load_jobs_for_run(self._runs[0]["databaseId"])

    def _load_jobs_for_run(self, run_id: int) -> None:
        self._selected_run_id = run_id
        jobs_table = self.query_one("#jobs-table", DataTable)
        jobs_table.clear()

        # Update header
        run_info = next((r for r in self._runs if r["databaseId"] == run_id), None)
        header = self.query_one("#jobs-header", Static)
        if run_info:
            header.update(
                f"Run #{run_id} · {run_info.get('workflowName', '')} · {run_info.get('headBranch', '')}"
            )

        try:
            self._jobs = gh_run_jobs(run_id)
        except RuntimeError as e:
            self.notify(f"Error: {e}", severity="error")
            return

        for job in self._jobs:
            icon = status_icon(job.get("status", ""), job.get("conclusion"))
            jobs_table.add_row(
                icon,
                job.get("name", "")[:25],
                job_duration(job),
                key=str(job.get("databaseId", "")),
            )

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        if event.data_table.id == "runs-table" and event.row_key:
            try:
                run_id = int(event.row_key.value)
                self._load_jobs_for_run(run_id)
            except (ValueError, TypeError):
                pass

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        if event.data_table.id == "runs-table":
            # Enter on runs table → focus jobs table
            jobs_table = self.query_one("#jobs-table", DataTable)
            if self._jobs:
                jobs_table.focus()
        elif event.data_table.id == "jobs-table":
            # Enter on jobs table → open log screen
            if self._selected_run_id is not None:
                idx = event.cursor_row
                job_name = self._jobs[idx]["name"] if idx < len(self._jobs) else "?"
                self.push_screen(LogScreen(self._selected_run_id, job_name))

    def action_refresh(self) -> None:
        self._load_runs()
        self.notify("Refreshed")

    def action_focus_runs(self) -> None:
        self.query_one("#runs-table", DataTable).focus()


if __name__ == "__main__":
    GHActionsApp().run()
