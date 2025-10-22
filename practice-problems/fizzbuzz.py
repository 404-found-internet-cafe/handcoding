from rich.console import Console
from rich.text import Text

# Initializing for Rich text
console = Console()

# You can change the value of below to experiment
MAXIMUM = 50

# Defining it here so I don't have to type them repeatedly
FIZZ = Text("Fizz", style="bold blue")
BUZZ = Text("Buzz", style="bold red")


def main():
    for num in range(1, MAXIMUM+1):
        output = fizz_buzz(num)
        console.print(output)


def fizz_buzz(num: int):
    """Returns the appropriate statement to print."""
    if num % 15 == 0:
        return FIZZ + BUZZ
    elif num % 3 == 0:
        return FIZZ
    elif num % 5 == 0:
        return BUZZ
    else:
        return num
    

if __name__ == "__main__":
    main()