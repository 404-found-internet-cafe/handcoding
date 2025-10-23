from rich.console import Console
from rich.prompt import IntPrompt
from rich.text import Text

# Initialize for rich text
console = Console()


minutes = IntPrompt.ask(
    Text("Enter a time in minutes", "bold blue")
)

# One minute is 60 seconds.
seconds = minutes * 60

# Format the response so that `seconds` is highlighted in yellow
response = Text.assemble(
    "You have ", (f"{seconds:,} seconds", "yellow bold"), ".",
    style="blue bold"
)

console.print(response)
