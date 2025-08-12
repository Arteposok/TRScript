import subprocess
from rich.console import Console


def run_command(c: Console, command: str) -> bool:
    """A safe and verbose command runner implementation"""
    try:
        c.print(f"[dim]Running: {command}[/]")
        _ = subprocess.run(command, shell=True, check=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        c.print(f"[red]Error: {e}[/]")
        return False
