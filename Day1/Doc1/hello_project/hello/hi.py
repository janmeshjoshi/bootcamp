from rich.console import Console

# Force color output (even if terminal isn't detected)
console = Console(force_terminal=True, color_system="truecolor")
console.print("[bold red]This MUST appear red now![/bold red]")