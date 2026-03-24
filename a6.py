print("Завдання 1:")
try:
    price = float(input("Введіть початкову ціну товару: "))
    discount = float(input("Введіть відсоток знижки: "))
    final_price = price * (1 - discount / 100)
    print("Фінальна ціна товару:", final_price)
except ValueError:
    print("Помилка: введено некоректне число")
finally:
    print("Операція завершена\n")


print("Завдання 2:")
try:
    usd = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну на євро: "))
    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")
    eur = usd * rate
    print(f"Сума в євро: {eur}")
except ValueError:
    print("Помилка: введено некоректне число")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Операція завершена\n")


print("Завдання 3:")
try:
    grades_input = input("Введіть оцінки студентів через пробіл: ")
    grades = [float(x) for x in grades_input.split()]
    average = sum(grades) / len(grades)
    print("Середнє значення оцінок:", average)
except ValueError:
    print("Помилка: введено некоректне число")
except ZeroDivisionError:
    print("Помилка: список оцінок порожній")
finally:
    print("Завершення обчислень\n")


print("Завдання 4: ")
balance = 1000
try:
    amount = int(input("Введіть суму для зняття: "))
    if amount % 10 != 0 or amount > balance:
        raise Exception("Некоректна сума для зняття")
    balance -= amount
    print("Транзакція успішна, залишок на рахунку:", balance)
except ValueError:
    print("Помилка: введено некоректне число")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Завершення транзакції\n")


print("Завдання 5:")
try:
    order_number = input("Введіть номер замовлення (ORDxxx): ")
    if not order_number.startswith("ORD") or not order_number[3:].isdigit():
        raise Exception("Неправильний формат номера замовлення")
    print("Номер замовлення коректний")
except Exception as e:
    print("Помилка:", e)
finally:
    print("Перевірка завершена\n")


print("Завдання 6:")
try:
    numbers_input = input("Введіть числа через пробіл: ")
    numbers = []
    for x in numbers_input.split():
        try:
            numbers.append(float(x))
        except ValueError:
            print(f"Попередження: '{x}' не є числом і буде пропущено")
    total = sum(numbers)
    average = total / len(numbers)
    print("Сума чисел:", total)
    print("Середнє значення:", average)
except ZeroDivisionError:
    print("Помилка: список чисел порожній")
finally:
    print("Завершення обробки даних\n")