import sys
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Confirm
from .utils import run_command


def checkpoint_func(
    c: Console, commit_msg: str | None = None, branch: str | None = None
):
    commit_msg = commit_msg or "Automated commit"
    branch = branch or "main"
    c.print(
        Align.center(
            Panel.fit(
                "[bold]Command that will run:[/]\n\n"
                + "git add .\n"
                + f"git commit -m [yellow]'{commit_msg}'[/]\n"
                + f"git push origin [cyan]{branch}[/]",
                title="checkpoint",
                border_style="cyan",
            )
        )
    )
    if not Confirm.ask("\nProceed?"):
        c.print("Aborted", style="yellow bold")
        c.print("Exiting", style="red")
        sys.exit(0)

    a = run_command(c, "git add .")
    b = run_command(c, "git commit -m '{commit_msg}'")
    d = run_command(c, "git push origin {branch}")
    if not (a and b and d):
        c.print("Not all commands exit successully", style="red bold")
        sys.exit(1)
    c.print("Thank you for using our tool", style="green bold")


if __name__ == "__main__":
    c = Console()
    checkpoint_func(c)
