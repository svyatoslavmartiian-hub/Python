"""
print(f"True and True = {True and True}")
print(f"False and True = {False and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")

print(f"True and True = {True or True}")
print(f"False or True = {False or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")

print(f"not False = {not False}")
print(f"not True = {not True}")
"""
'''
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(4))
print(bool(10.5))
print(bool("hello"))

name = None
print(bool(name))
'''


'''
temperature = int(input("Яка зараз температура на вулиці?"))

if temperature <= 0:
    print("Одягаємо зимову шапку")
    print("Одягаємо зимову шубу")
    print("Беремо рукавички")
elif temperature > 0 and temperature < 15:
    print("Одягаємо шапку")
    print("Одягаємо куртку")
else: 
    print('Вдягаємо футболку')
    print('Вдягаємо кепку')

print("Виходимо на вулицю")  
'''

'''



number = int(input("Ведіть ціле число:"))

print(f"{number} > 10 {number > 10}")
print(f"{number} < 10 {number < 10}")
print(f"{number} >= 10 {number >= 10}")
print(f"{number} <= 10 {number <= 10}")
print(f"{number} == 10 {number == 10}")
print(f"{number} != 10 {number != 10}")




PI = 3.14






can_pinguins_swim = True
can_pinguins_fly = False
print(f"Пінгвіни вміють плавати: {can_pinguins_swim}")
print(f"Пінгвіни вміють літати: {can_pinguins_fly}")
print(type(can_pinguins_fly))
print(type(can_pinguins_swim))

'''
'''
number = int(input("Ведіть ціле число:"))
if number >- 10 and number<-20:
    print(f"{number} входить в діапазон від 10 до 20")
else:
    print(f"{number} не входить в діапазон від 10 до 20")
'''
'''
number1 = float(input("Ведіть перше число "))
number2 = float(input("Ведіть друге число "))
operation = input("Ведіть оператор(+,-,*,/) ")

match operation:
    case "+":
        print(f"{number1} + {number2} =  {number1 + number2} ")
    case "-":
        print(f"{number1} - {number2} =  {number1 - number2} ")
    case "*":
        print(f"{number1} * {number2} =  {number1 * number2} ")
    case "/":
        if number2 == 0:
            print("Не можна ділити на нуль")
        else:
            print(f"{number1} / {number2} =  {number1 / number2} ")

'''
      


'''
if operation == "+":
    print(f"{number1} + {number2} =  {number1 + number2} ")
elif operation == "-":
   print(f"{number1} - {number2} =  {number1 - number2} ")
elif operation == "*":
   print(f"{number1} * {number2} =  {number1 * number2} ")
elif operation == "/":
    if number2 == 0:
        print("Не можна ділити на нуль")
    else:
        print(f"{number1} / {number2} =  {number1 / number2} ")

else:
   print("Невідомий оператор")

'''















