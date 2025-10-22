from rich.console import Console
from rich.prompt import IntPrompt
from rich.text import Text

# Initialize for Rich text
console = Console()

def main():
	time = IntPrompt.ask(Text("Enter a time in seconds", "bold blue"))
	seconds_to_minutes(time)


def seconds_to_minutes(seconds: int):
	# Convert the seconds to minutes
	minutes = seconds // 60
	# Collect the remainder
	extra_seconds = seconds % 60

	# Formatting the text again
	response = Text.assemble(
		"You have ",
		(f"{minutes} minutes", "yellow bold"),
		" and ",
		(f"{extra_seconds} seconds", "yellow bold"),
		".",
		style="bold blue"
	)
	console.print(response)


if __name__ == "__main__":
	main()