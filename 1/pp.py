try:
    price = float(input("Введіть початкову ціну товару: "))
    discount = float(input("Введіть відсоток знижки: "))

    final_price = price - (price * discount / 100)

    print("Фінальна ціна:", final_price)

except ValueError:
    print("Помилка! Потрібно вводити тільки числа.")




try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну (1 долар = ? євро): "))

    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")

    euros = dollars * rate
    print("Сума в євро:", euros)

except ValueError:
    print("Помилка! Потрібно вводити тільки числа.")

except Exception as e:
    print("Помилка:", e)

finally:
    print("Операцію завершено.")