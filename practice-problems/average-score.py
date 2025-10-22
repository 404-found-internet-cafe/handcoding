from rich.console import Console
from rich.prompt import IntPrompt
from rich.text import Text

# Initializing for Rich text
console = Console()

# If you want to calculate more scores, change here.
SCORE_COUNT = 3


scores = []
for i in range(SCORE_COUNT):
    score = IntPrompt.ask(Text(f"Score {i+1}", "bold blue"))
    scores.append(score)


average = sum(scores) / SCORE_COUNT

result = Text.assemble(("Average score: ", "bold blue"), (f"{average:,.2f}", "bold yellow"))
console.print(result)
