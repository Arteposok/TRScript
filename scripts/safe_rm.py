import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm


def send_to_trash(path: Path) -> bool:
    """Move a file to trash on all platforms"""
    try:
        from send2trash import send2trash

        send2trash(str(path))
        return True
    except ImportError:
        raise ImportError(
            'Install "send2trash" with pip install send2trash'
            + "(or ours package amanger)"
        )


def rm_safe(c: Console, *targets: str, force: bool = False) -> None:
    """A safe way to 'delete' files"""
    if not targets:
        c.print("[red]Error: No targets specified[/]")
        sys.exit(1)

    paths = [Path(t).absolute() for t in targets]
    missing = [p for p in paths if not p.exists()]

    if missing:
        c.print(f"[red]Error: Not found[/] {[str(p) for p in missing]}")
        sys.exit(1)

    c.print(
        Panel.fit(
            "\n".join(f"• [yellow]{p}[/]" for p in paths),
            title="[bold]Targets to move to trash[/]",
            border_style="red",
        )
    )
    if not force and not Confirm.ask("\nProceed?", default=False):
        c.print("[yellow]Aborted[/]")
        c.print("[red]Exiting[/]")
        sys.exit(0)
    try:
        for p in paths:
            _ = send_to_trash(p)
        c.print(f"[green]✓ Moved to trash![/]", justify="center")
    except Exception as e:
        c.print(f"[red]Error: {e}[/]")
        sys.exit(1)
