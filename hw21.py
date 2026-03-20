
dictionary = {
    "cat": "кіт",
    "dog": "собака",
    "apple": "яблуко",
    "car": "машина",
    "house": "будинок"
}

word = input("Введіть слово англійською: ").lower()

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слово не знайдено")




games = {
    "Minecraft": 10,
    "CS2": 5,
    "Among Us": 15,
    "Dota 2": 10,
    "FIFA": 2
}

friends = int(input("Скільки у вас друзів? "))
total_players = friends + 1

print("Ігри, де можуть грати всі разом:")

for game, max_players in games.items():
    if total_players <= max_players:
        print(game)