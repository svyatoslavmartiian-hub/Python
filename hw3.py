'''
number1 = float( input("Ведіть перше число:"))
number2 = float( input("Ведіть перше число:"))
number3 = float( input("Ведіть перше число:"))
print(f"{number1} + {number2} + {number3} = {number1 + number2 + number3}")
print(f"{number1} * {number2} * {number3} = {number1 * number2 * number3}")

diagonal1 = float(input("Ведіть першу діагональ:"))
diagonal2 = float(input("Ведіть другу діагональ:"))
print(f"Площа ромба = {diagonal1 * diagonal2 / 2}")

salary = float(input("Ведіть вашу зарплату:"))
credit = float(input("Ведіть суму щомісячного кредиту:"))
debt = float(input("Ведіть суму заборгованості за комунальні послуги:"))
print(f"Залишок коштів = {salary - credit - debt}")

distance = float( input("Ведіть відстань у км:"))
expense = float( input("Ведіть витрату палива на 100км:"))
price = float( input("Ведіть ціну за паливо(1л):"))
print(f"Вартість поїздки скадатиме: {(expense / 100) * distance * price}")

price2 = float(input("Ведіть загальну суму:"))
quantity = float(input("Ведіть кількість осіб:"))
print(f"Кожна людина повина заплатити по: {(price2 * 15 / 100 + price2) / quantity}")
'''
cost = float(input("Ведіть вартість оренди за 1 день:"))
quantity2 = float(input("Ведіть кількість днів оренди:"))
pledge = float(input("Ведіть суму застави:"))
print(f"Загальна вартість оренди = {cost * quantity2 + pledge}")
print(f"Вартість оренди після повернення автомобіля: {cost * quantity2}")
print(f"Вартість за день складатиме: {cost * quantity2 / quantity2}")