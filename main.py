import click
from rich.console import Console

from scripts.checpoint import checkpoint_func
from scripts.safe_rm import rm_safe

c = Console()


@click.group()
def main():
    pass


@main.command()
@click.option("-m", "message")
@click.option("--branch")
def checkpoint(message: str | None, branch: str | None):
    checkpoint_func(c, message, branch)


@main.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("files", nargs=-1, type=click.UNPROCESSED)
def safe_rm(files: list[str]):
    rm_safe(c, *files)


if __name__ == "__main__":
    main()
