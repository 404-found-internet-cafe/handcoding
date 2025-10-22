from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()


LIKES = [
    "eyes",
    "dimples",
    "shirt",
    "fingers",
    "the way that you smell", # ???
]

like = Prompt.ask(Text("Tell me what I like", "bold blue"))


if like.lower() in LIKES:
    console.print(Text.assemble(
        ("Correct! I do like ", "bold green"),
        (like, "bold yellow") 
    ))
else:
    console.print(Text.assemble(    
        ("I don't actually like ", "bold red"),
        (like, "bold yellow") 
    ))