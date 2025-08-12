import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt


def checkpoint(c: Console, commitM: str | None = None, branch: str | None = None):
    if commitM is None:
        commitM = "Automated commit"
    if branch is None:
        branch = "main"
    c.print(
        Align.center(
            Panel.fit(
                f'This will execute `git add . && git commit -m "{commitM}" && git push -u origin {branch}`',
            ),
        ),
        style="bold",
    )
    yes = Prompt.ask("Execute?", console=c, choices=["Y", "n"], default="n")
    if yes == "Y":
        _ = subprocess.run(
            "git add .",
            shell=True,
            check=True,
        )
        _ = subprocess.run(
            f'git commit -m "{commitM}"',
            shell=True,
            check=True,
        )
        _ = subprocess.run(
            f"git push -u origin {branch}",
            shell=True,
            check=True,
        )
        c.print("Thank you for using our tool", style="green bold")


if __name__ == "__main__":
    c = Console()
    checkpoint(c)
