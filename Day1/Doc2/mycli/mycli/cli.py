import typer
app = typer.Typer()
@app.command()
def hello(name: str = typer.Argument("World")):
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str = typer.Argument("World"), formal: bool = typer.Option(False, "--formal")):
    """Say goodbye to someone"""
    if formal:
        typer.echo(f"Goodbye, Mr./Ms. {name}. Have a nice day!")
    else:
        typer.echo(f"Bye {name}!")

if __name__ == "__main__":
    app()