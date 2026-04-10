# 1
# def print_quote():
#     print('"Don\'t let the noise of others\' opinions')
#     print(' drown out your own inner voice."')
#     print('       Steve Jobs')

# print_quote()


# 2
# def show_odd_numbers(a, b):
#     start = min(a, b)
#     end = max(a, b)
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             print(i)

# show_odd_numbers(1, 10)

# 3

# def draw_line(length, direction, symbol):
#     if direction == "horizontal":
#         print(symbol * length)
#     elif direction == "vertical":
#         for i in range(length):
#             print(symbol)

# draw_line(5, "horizontal", "*")
# draw_line(3, "vertical", "|")


# 4
# def get_max(a, b, c, d):
#     maximum = a
#     if b > maximum:
#         maximum = b
#     if c > maximum:
#         maximum = c
#     if d > maximum:
#         maximum = d
#     return maximum

# print(get_max(10, 5, 25, 3))


# 5
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# print(is_prime(7))  
# print(is_prime(10)) 

# 6
# def is_lucky_number(num):
#     s = str(num)
#     if len(s) != 6:
#         return False
    
#     sum1 = int(s[0]) + int(s[1]) + int(s[2])
#     sum2 = int(s[3]) + int(s[4]) + int(s[5])
    
#     if sum1 == sum2:
#         return True
#     else:
#         return False

# print(is_lucky_number(123420))
# print(is_lucky_number(723422)) 


# 1

# num1 = int(input("Число 1 "))
# num2 = int(input("Число 2 "))
# num3 = int(input("Число 3 "))

# print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
# print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")

# 2

# num1 = int(input("Перша діагональ "))
# num2 = int(input("Друга діагональ "))

# print(f"Площа ромба = {num1 * num2 / 2}")
 
# 3

# num1 = int(input("Ведіть свою зарплату  "))
# num2 = int(input("Ведіть суму платежу за кредит "))
# num3 = int(input("Ведіть заборгованість за комунальні послуги"))

# print(f"Залишок: = {num1 - num2 - num3}")

# 4

# num1 = int(input("Ведіть відстань у км "))
# num2 = int(input("Ведіть витрату "))
# num3 = int(input("Ведіть ціну за бензин"))

# print(f"Вартість: = {num1 / 100 * num2 * num3}")

# 5

# num1 = int(input("Ведіть загальну суму "))
# num2 = int(input("Ведіть кількість осіб "))

# print(f"Кожен має заплотити: = {(num1 / 100 * 15 + num1) / num2}")

# 6


# num1 = int(input("Ведіть ціну за день "))
# num2 = int(input("Ведіть кількість днів "))
# num3 = int(input("Ведіть суму застави "))

# print(f"Загальна сума {num1 * num2 + num3}")
# print(f"Сума після повернення  {num1 * num2}")
# print(f"Ціна за один день {num1}")
