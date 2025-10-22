from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

# Initialize for rich text
console = Console()

# Ask for the name
your_name = Prompt.ask(
    Text("What is your name", style="bold blue")
)

# Formatting text so that `your_name` is highlighted in yellow
response = Text.assemble(
    "Hello, ", (your_name.title(), "bold yellow"), ".",
    style="bold blue"
)

console.print(response)