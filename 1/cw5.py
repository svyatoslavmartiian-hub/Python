'''
number = int(input("Ведіть ціле число: "))

# Скорочена форма if 
#if number % 2 == 0: print(f"Число {number} парне")

print(f"Число {number} парне") if number % 2 == 0 else print(f"Число {number} не парне")

num1 = 10
num2 = 15

print(f"num1") if num1 > num2 else print(f"num2") if num2 > num1 else print("==")




# 10 + 12 - бінарний оператор
# -(-10) - унарний 


age = 18

if age < 18: 
    pass
else:
    print ("Можете голосувати")
    '''
"""
day = int(input("Ведіть номер дня: "))
match day:
    case 1: print("Понеділок")
    case 2: print("Вівторок")
    case 3: print("Середа")
    case 4: print("Четвер")
    case 5: print("П\'ятниця")
    case 6: print("Субота")
    case 7: print("Неділя")
    case _: print("Некоректний номер дня")

"""
'''
month = int(input("Ведіть номер місяця: "))

match month: 
    case 12 | 1 | 2: print("Зима")
    case 3 | 4 | 5: print("Весна")
    case 6 | 7 | 8: print("Літо")
    case 9 | 10 | 11: print("Осінь")
    case _: print("Некоректний номер місяця") 

day = int(input("Ведіть номер дня: "))

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("Будній день в січні")
    case 6 | 7  if month == 1:
        print("Вихідний день в січні")
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("Будній день в лютому")
    case 6 | 7  if month == 2:
        print("Вихідний день в лютому")
'''








"""
day = int(input("Ведіть номер дня: "))

if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Некоректний номер дня")
"""
"""
num1 = float(input("Ведіть перше число: "))
num2 = float(input("Ведіть друге число: "))
action = input("Ведіть знак операції (+, -, *, /, %, //, **): ")

match action: 
    case "+": print(f"{num1} + {num2} = {num1 + num2}")
    case "-": print(f"{num1} - {num2} = {num1 - num2}")
    case "*": print(f"{num1} * {num2} * {num1 + num2}")
    case "/": 
        if num2 == 0:
            print("Неможна ділити на 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    case "%": 
        if num2 == 0:
            print("Неможливо знайти остачу,оскільки на 0 неможна ділити!")
        else:
            print(f"{num1} % {num2} = {num1 % num2}")
    case "//":
        if num2 == 0:
            print("Неможна ділити на 0!")
        else: 
            print(f"{num1} // {num2} = {num1 // num2}")
    case "**": print(f"{num1} ** {num2} ** {num1 + num2}")
    case _: print("Некоректна операція!")
    """



