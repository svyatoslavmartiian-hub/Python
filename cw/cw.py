# import cowsay

# from art import *

# tprint("Hello")

# art_text = text2art("Hello", font="block", chr_ignore=True )
# print(art_text)


# # cowsay.trex("RRAAAAAAA")

from rich.console import Console
from rich.table import Table
console = Console()

table = Table(title="Список студентів")
table.add_column("Ім'я", style="cyan")
table.add_column("Курсовий проєкт", style="magenta")

table.add_row("Антон", "Чат-бот")
table.add_row("Марія", "Гра на пайтон")

console.print(table)