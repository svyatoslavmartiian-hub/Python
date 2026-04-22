# for i in range(1,8):
#     print(f"7 * {i} = {i * 7}")


# for j in range(1,10):
#     for x in range(1,11):
#         print(f"{j} * {x} = {j * x}")



# n = int(input("Ведіть кількість чисел:"))

# num1 = float(input("Ведіть перше число"))
# max_num = num1

# for i in range(2, n + 1):
#     num2 = float(input(f"Ведіть {i} число"))
#     if num2 > max_num:
#         max_num = num2

# print(max_num)

# import random

# random1 = random.randint(1,500)
 
# num = int(input("Ведіть число: "))

# for i in range(2, num + 1):
#     exit = print("Ведіть 0 щоб вийти, Enter щоб продовжити.")
#     if exit == 0:
#         break
#     if num == random1:
#         print("Ти вгадав!")
#         print(f"Кількість спроб {i}")
#         break
#     num = int(input("Ведіть число: "))
#     if num < random1:
#         print("Число більше! ")
#     else:
#         print("Число меньше")


figura = int(input("Ведіть 1 - щоб намалювати квадрат, 2 - прямокутник"))
if figura == 1: value = int(input("Ведіть розмір сторони квадрату"))
elif figura == 2: 
     value2 = int(input("Ведіть ширину прямокутника"))
     value3 = int(input("Ведіть довжину прямокутника"))
n = input("Ведіть фігуру ")

if figura == 1:
    for i in range(value):
        print((n + ' ') * value)
elif figura == 2:
    for i in range(value2):
            print((n + " " ) * value3)