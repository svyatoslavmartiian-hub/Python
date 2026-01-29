# age = int(input("Ведіть ваш вік "))

# if age > 18:
#     print("Ви можете купити пиво")
# else:
#     print("Дітям пиво не можна")

# number1 = 10
# number2 = 12
# if number1 > number2:
#     print(number1)
# elif number1 < number2: 
#     print(number2)
# else:
#     print("Числа однакові")

# needed_potates = int(input("Ведіть ількість потрібної картоплі"))

# peeled_potates = 0

# while peeled_potates < needed_potates:
#     print("Чистимо картоплю")
#     is_rotten = input("Картопля гнила?")
#     if is_rotten == "так":
#         print("Викидаємо!")
#         continue
#     print("Чистимо картоплю...")
#     print("готово")
#     peeled_potates +=1




# print(f"Почистили {peeled_potates} штук картоплі")


while True:
    num1 = float(input("Ведіть перше число"))
    num2 = float(input("Ведіть друге число"))
    action = input("Оберіть операцію (+, -, *, /): ")

    match action:
            case "+":
                print(f"{num1} + {num2} = {num1 + num2}")
            case "-":
                print(f"{num1} - {num2} = {num1 - num2}")
            case "*":
                print(f"{num1} * {num2} = {num1 * num2}")
            case "/":
                if num2 == 0:
                     print("Неможна ділити на нуль")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            case _:
                print("Некоректна операція!")
    q = input("Ведіть q щоб завершити.Натисніть Enter щоб продовжити.")
    if q == "q":
         break
