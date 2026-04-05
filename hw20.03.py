# # 1
# lines = []
# for i in range(3):
#     line = input(f"Введіть рядок {i+1}: ")
#     lines.append(line)

# with open("data.txt", "w", encoding="utf-8") as file:
#     for line in lines:
#         file.write(line + "\n")

# print("Дані успішно записані у файл data.txt")
# 2

import re
from collections import Counter

try:
    with open("log.txt", "r", encoding="utf-8") as file:
        text = file.read().lower()
        # Використовуємо регулярні вирази, щоб знайти лише слова
        words = re.findall(r'\b\w+\b', text)

    common_words = Counter(words).most_common(10)

    with open("word_stats.txt", "w", encoding="utf-8") as out_file:
        for word, count in common_words:
            out_file.write(f"{word}: {count}\n")
    
    print("Статистика збережена у word_stats.txt")

except FileNotFoundError:
    print("Помилка: Файл log.txt не знайдено.")

# 3

import os

FILENAME = "orders.txt"

def load_orders():
    if not os.path.exists(FILENAME):
        return []
    orders = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            orders.append(line.strip().split(","))
    return orders

def save_orders(orders):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for order in orders:
            f.write(",".join(order) + "\n")

def main():
    while True:
        print("\n--- Меню ---")
        print("1. Додати нове замовлення")
        print("2. Переглянути всі замовлення")
        print("3. Пошук замовлення за номером")
        print("4. Оновити замовлення")
        print("5. Видалити замовлення")
        print("6. Вихід")
        
        choice = input("Оберіть дію: ")

        if choice == "1":
            id = input("Номер замовлення: ")
            name = input("Назва товару: ")
            qty = input("Кількість: ")
            price = input("Ціна: ")
            orders = load_orders()
            orders.append([id, name, qty, price])
            save_orders(orders)
            print("Замовлення додано!")

        elif choice == "2":
            orders = load_orders()
            for o in orders:
                print(f"ID: {o[0]}, Товар: {o[1]}, К-сть: {o[2]}, Ціна: {o[3]}")

        elif choice == "3":
            id_search = input("Введіть номер замовлення: ")
            orders = load_orders()
            found = False
            for o in orders:
                if o[0] == id_search:
                    print(f"Знайдено: {o}")
                    found = True
                    break
            if not found: print("Не знайдено.")

        elif choice == "4":
            id_upd = input("Номер замовлення для оновлення: ")
            orders = load_orders()
            for o in orders:
                if o[0] == id_upd:
                    o[2] = input("Нова кількість: ")
                    o[3] = input("Нова ціна: ")
                    save_orders(orders)
                    print("Оновлено.")
                    break

        elif choice == "5":
            id_del = input("Номер замовлення для видалення: ")
            orders = load_orders()
            new_orders = [o for o in orders if o[0] != id_del]
            if len(orders) != len(new_orders):
                save_orders(new_orders)
                print("Видалено.")
            else:
                print("Замовлення не знайдено.")

        elif choice == "6":
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()