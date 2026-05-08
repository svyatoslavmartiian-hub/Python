import random

def get_status_message(attempts):
    """Повертає текстовий статус (Пункт 4: Dictionary)"""
    messages = {
        6: "Ви ще не помилялися.",
        5: "Перша помилка. Залишилося 5 спроб!",
        4: "Залишилося 4 спроби.",
        3: "Половина спроб вичерпана. Залишилось 3 спроби!",
        2: "Залишилося 2 спроби.",
        1: "Остання спроба!",
        0: "Спроб більше немає."
    }
    return messages.get(attempts, "Стан невідомий")

def save_game_result(status, word):
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"Результат: {status} | Слово: {word}\n")
    except Exception as e:
        print(f"Помилка збереження: {e}")

def play_game():
    config = (6, "words.txt") 
    
    try:
        with open(config[1], "r", encoding="utf-8") as f:
            words = [line.strip() for line in f.readlines() if line.strip()]
        if not words: return print("Файл порожній!")
    except FileNotFoundError:
        return print(f"Файл {config[1]} не знайдено!")

    word_to_guess = random.choice(words).lower()
    guessed_letters = set()
    attempts = config[0]

    print("\n--- ГРА ПОЧАЛАСЯ ---")

    while attempts > 0:
        print(f"\nСтатус: {get_status_message(attempts)}")
        
        display = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        print(f"Слово: {display}")
        print(f"Залишилось спроб: {attempts}")

        if "_" not in display:
            print(f"ПЕРЕМОГА! Слово: {word_to_guess.upper()}")
            save_game_result("ПЕРЕМОГА", word_to_guess)
            return

        guess = input("Введіть літеру: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Помилка: потрібна одна літера!")
        elif guess in guessed_letters:
            print("Ви вже це вводили!")
        else:
            guessed_letters.add(guess)
            if guess not in word_to_guess:
                attempts -= 1
                print("Не вгадали!")
            else:
                print("Є така літера!")

    print(f"\nВИ ПРОГРАЛИ. Слово було: {word_to_guess.upper()}")
    save_game_result("ПРОГРАШ", word_to_guess)

if __name__ == "__main__":
    while True:
        print("\n1. Грати | 2. Історія | 3. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1": play_game()
        elif choice == "2":
            try:
                with open("history.txt", "r", encoding="utf-8") as f:
                    print("\nІСТОРІЯ:\n" + f.read())
            except FileNotFoundError:
                print("Історія порожня.")
        elif choice == "3": break