from rich.console import Console
from rich.prompt import IntPrompt
from rich.text import Text

# Initialize for Rich text
console = Console()

# Constants
ODD = Text("odd", "bold yellow")
EVEN = Text("even", "bold green")

def main():
    number = IntPrompt.ask(Text("Give me a number", "bold blue"))

    response = Text.assemble(
        f"{number} is an ", odd_or_even(number), " number.",
        style="bold blue"
    )
    console.print(response)
    

def odd_or_even(num: int):
    # Modulo Operator
    if num % 2 == 0:
        return ODD
    else:
        return EVEN
    

if __name__ == "__main__":
    main()