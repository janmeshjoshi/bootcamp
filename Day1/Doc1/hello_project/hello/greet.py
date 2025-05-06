from rich import print
from rich.console import Console

def say_hello(name="World"):
    console = Console(force_terminal=True, color_system="truecolor")
    console.print("[bold red] This is a rich styled message[/bold red]")
