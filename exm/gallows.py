import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def draw_hangman(attempts):
    stages = {
        6: "  +---+\n      |\n      |\n      |\n     ===",
        5: "  +---+\n  O   |\n      |\n      |\n     ===",
        4: "  +---+\n  O   |\n  |   |\n      |\n     ===",
        3: "  +---+\n  O   |\n /|   |\n      |\n     ===",
        2: "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
        1: "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
        0: "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ==="
    }
    return stages.get(attempts, "")

def save_game_result(status, word):
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"{status}|{word}\n")
    except Exception:
        pass

def show_history():
    table = Table(title="ІСТОРІЯ ІГОР", header_style="bold cyan")
    table.add_column("№", style="dim")
    table.add_column("Результат", justify="center")
    table.add_column("Слово", justify="right", style="green")

    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if "|" in line:
                    status, word = line.strip().split("|")
                    color = "green" if "ПЕРЕМОГА" in status else "red"
                    table.add_row(str(i), f"[{color}]{status}[/{color}]", word.upper())
        console.print(table)
    except FileNotFoundError:
        print("Історія поки що порожня.")

def play_game():
    config = (6, "words.txt")
    try:
        with open(config[1], "r", encoding="utf-8") as f:
            words = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        return

    word_to_guess = random.choice(words).lower()
    guessed_letters = set()
    attempts = config[0]

    console.print(Panel.fit("[bold cyan]ГРА ПОЧАЛАСЯ[/bold cyan]", border_style="cyan"))

    while attempts > 0:
        console.print(draw_hangman(attempts))
        
        display = ""
        for l in word_to_guess:
            if l in guessed_letters:
                display += f"[bold green]{l}[/bold green] "
            else:
                display += "_ "
        
        console.print(f"\nСЛОВО: {display}")
        console.print(f"Залишилось спроб: [bold red]{attempts}[/bold red]")

        if "_" not in display:
            console.print(Panel(f"[bold green]ПЕРЕМОГА![/bold green]\nВи вгадали слово: {word_to_guess.upper()}", border_style="green"))
            save_game_result("ПЕРЕМОГА", word_to_guess)
            return

        user_input = console.input("\n[bold magenta]Введіть літеру або слово:[/bold magenta] ").lower().strip()

        if len(user_input) > 1:
            if user_input == word_to_guess:
                console.print(Panel(f"[bold yellow]БЛИСКУЧЕ![/bold yellow]\nСлово {word_to_guess.upper()} вгадано!", border_style="yellow"))
                save_game_result("ПЕРЕМОГА (СЛОВО)", word_to_guess)
                return
            else:
                attempts -= 1
        elif len(user_input) == 1 and user_input.isalpha():
            if user_input not in guessed_letters:
                guessed_letters.add(user_input)
                if user_input not in word_to_guess:
                    attempts -= 1

    console.print(draw_hangman(0))
    console.print(Panel(f"[bold red]ПРОГРАШ[/bold red]\nСлово було: {word_to_guess.upper()}", border_style="red"))
    save_game_result("ПРОГРАШ", word_to_guess)

if __name__ == "__main__":
    while True:
        menu_table = Table(show_header=False, border_style="yellow")
        menu_table.add_column("ID", justify="center", style="bold yellow")
        menu_table.add_column("Action")

        menu_table.add_row("[1]", "Грати")
        menu_table.add_row("[2]", "Історія")
        menu_table.add_row("[3]", "Вихід")

        console.print("\n", menu_table)
        choice = console.input("[bold yellow]Ваш вибір:[/bold yellow] ")
        
        if choice == "1":
            play_game()
        elif choice == "2":
            show_history()
        elif choice == "3":
            break