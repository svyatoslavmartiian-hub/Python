"""
#Завдання 1
num1 = float(input("Ведіть бал за іспит: "))

if num1 < 100 and num1 >= 90:
    print("Відмінно")
elif num1 < 89 and num1 >= 70:
    print("Добре")
elif num1 < 69 and num1 >= 50:
    print("Задовільно")
elif num1 < 50:
    print("Незадовільно")
else:
    print("Ведіть число в діапазоні від 0 до 100.")

#Завдання 2 

num2 = float(input("Ведіть свій стаж роботи "))
num3 = float(input("Ведіть свою заробітну плату "))
 
if num2 < 1:
    print("Премія не передбачена")
elif num2 < 3 and num2 >= 1:
    print("Премія 5% від зарплати")
elif num2 < 5 and num2 >= 3:
    print("Премія 10%.")
else:
    print("Премія 15%.")
#Завдання 3

num4 = int(input("Введіть чотиризначне число: "))

num5 = num4 // 1000 + (num4 // 100) % 10 + (num4 // 10) % 10 + num4 % 10

if num5 % 2 == 0:
    print("Сума цифр парна")
else:
    print("Сума цифр непарна")
"""
num6 = int(input("Ведіть ціле шестизначне число "))
num7 = num6 // 100000 + (num6 // 10000) % 10 + (num6 // 1000) % 10
num8 = num6 // 100 % 10 + (num6 // 10) % 10 + num6 % 10
if num6 < 100000 and num6 > 999999:
    print("Це не шестизначне число")
elif num7 == num8:
    print("Це число щасливе")
else:
    print("Це число не щасливе")