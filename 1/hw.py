
num1 = int(input("Ведіть номер дня тиждня: "))
if num1 == 1:
    print("Понеділок")
elif num1 == 2:
    print("Вівторок")
elif num1 == 3:
    print("Середа")
elif num1 == 4:
    print("Четвер")
elif num1 == 5:
    print("П'ятниця")
elif num1 == 6:
    print("Субота")
elif num1 == 7:
    print("Неділя")
else:
    print("Некоректний номер дня.")





num2 = int(input("Ведіть номер місяця: "))
if num2 == 1:
    print("Січень")
elif num2 == 2:
    print("Лютий")
elif num2 == 3:
    print("Березень")
elif num2 == 4:
    print("Квітень")
elif num2 == 5:
    print("Травень")
elif num2 == 6:
    print("Червень")
elif num2 == 7:
    print("Липень")
elif num2 == 8:
    print("Серпень")
elif num2 == 9:
    print("Вересень")
elif num2 == 10:
    print("Жовтень")
elif num2 == 11:
    print("Листопад")
elif num2 == 12:
    print("Грудень")
else:
    print("Некоректний номер місяця.")



num3 = int(input("Ведіть суму покупки: "))
num4 = int(input("Ведіть свій вік: "))
if num4 <= 0:
    print("Некоректний вік")
elif num4 < 18:
    print(f"Ваша знижка дорівнює 10%, до сплати  {num3 - (num3 * 10 / 100)}$")
elif num4 < 60 and num4 >= 18:
    print(f"Ваша знижка дорівнює 5%, до сплати {num3 - (num3 * 5 / 100)}$")
else:
    print(f"Ваша знижка дорівнює 15%, до сплати {num3 - (num3 * 15 / 100)}$")



num5 = int(input("Введіть оцінку з першого предмета: "))
num6 = int(input("Введіть оцінку з другого предмета: "))
num7 = int(input("Введіть оцінку з третього предмета: "))

if num5 == 2:
    print("Незадовільно", end="")
elif num6 == 2:
    print("Незадовільно", end="")
elif num7 == 2:
    print("Незадовільно")
elif num5 >= 4:
    if num6 >= 4:
        if num7 >= 4:
            print("Відмінно")
else:
    print("Некоректно написено оцінку(1-5)!")




num8 = int(input("Введіть оцінку з першого предмета: "))
num9 = int(input("Введіть оцінку з другого предмета: "))
num10 = int(input("Введіть оцінку з третього предмета: "))
num11 = int(input("Введіть оцінку з четвертого предмета: "))

if num8 == 2:
    print("Недопуск до іспиту", end="")
elif num9 == 2:
    print("Недопуск до іспиту", end="")
elif num10 == 2:
    print("Недопуск до іспиту", end="")
elif num11 == 2:
    print("Недопуск до іспиту")
elif num8 >= 4:
    if num9 >= 4:
        if num10 >= 4:
            if num11 >= 4:
                print("Допуск до іспиту з відзнакою")
elif num8 == 3:
    if num9 == 3:
        if num10 == 3:
            if num11 ==3:
                print("Допуск до іспиту")
else:
    print("Некоректно написено оцінку(1-5)!")



num12 = int(input("Ведіть вік автомобіля: "))
num13 = int(input("Ведіть пробіг: "))

if num12 < 3 and num13 < 30000: 
    print("Автомобіль у відмінному стані")
elif num12 < 10 and num13 < 100000: 
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")
