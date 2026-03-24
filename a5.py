import random
import math

print("Завдання 1:")
try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    result = a / b
    print("Результат ділення:", result)
except ValueError:
    print("Помилка: введене значення не є числом")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе")
finally:
    print("Операція завершена\n")


print("Завдання 2:")
lst = [10, 20, 30, 40, 50]
try:
    idx = int(input(f"Введіть індекс елемента (0-{len(lst)-1}): "))
    print("Елемент списку:", lst[idx])
except ValueError:
    print("Помилка: індекс не є числом")
except IndexError:
    print("Помилка: індекс поза межами списку")
finally:
    print("Операція завершена\n")


print("Завдання 3:")
try:
    sales_input = input("Введіть продажі через пробіл (наприклад, '100 250 300'): ")
    sales = [float(x) for x in sales_input.split()]
    total = sum(sales)
    print("Загальна сума продажів:", total)
except ValueError:
    print("Помилка: введено некоректні дані")
finally:
    print("Обробка завершена\n")


print("Завдання 4:")
try:
    num = float(input("Введіть число для обчислення квадратного кореня: "))
    if num < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    sqrt_num = math.sqrt(num)
    print("Квадратний корінь:", sqrt_num)
except ValueError:
    print("Помилка: введене значення не є числом")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Обчислення завершено\n")


print("Завдання 5:")
try:
    item_input = input("Введіть дані про товар (назва, ціна, кількість): ")
    parts = [x.strip() for x in item_input.split(',')]
    name = parts[0]
    price = float(parts[1])
    quantity = float(parts[2])
    print(f"Товар: {name}, Ціна: {price}, Кількість: {quantity}")
except ValueError:
    print("Помилка: не вдалося перетворити ціну або кількість на число")
finally:
    print("Парсинг завершено\n")


print("Завдання 6:")
def connect_to_server():
    if random.choice([True, False]):
        return "Підключення успішне"
    else:
        raise ConnectionError("Помилка підключення")

try:
    msg = connect_to_server()
    print(msg)
except ConnectionError:
    print("Не вдалося підключитися до сервера")
finally:
    print("Спробу завершено")