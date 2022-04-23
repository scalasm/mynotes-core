"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Mynotes Core."""
    print("Hello MyNotes Core!")

if __name__ == "__main__":
    main(prog_name="mynotes-core")  # pragma: no cover
