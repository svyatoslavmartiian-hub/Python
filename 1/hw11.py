# num1 = int(input("Ведіть перше число "))
# num2 = int(input("Ведіть друге число "))
# num3 = num1
# print("Всі числа кратні 7:")
# while num3 <= num2:
#     if num3 % 7 == 0:
#         print(num3)
#     num3 += 1






# left = int(input('Введіть ліву межу діапазону: '))
# right = int(input('Введіть праву межу діапазону: '))

# if left > right:
#     left, right = right, left

# counter = left

# countMultiply5 = 0

# print("Усі числа діапазону: ")
# while counter <= right:
#     print(counter, end=' ')
#     if counter % 5 == 0: countMultiply5 += 1
#     counter += 1

# counter = right
# print("\nУсі числа діапазону в спадному порядку: ")
# while counter >= left:
#     print(counter, end=' ')
#     counter -= 1

# counter = left
# print("\nУсі числа кратні 7: ")
# while counter <= right:
#     if counter % 7 == 0: print(counter, end=' ')
#     counter += 1

# print('\nКількість чисел, кратних 5:', countMultiply5)







# left2 = int(input('Введіть ліву межу діапазону: '))
# right2 = int(input('Введіть праву межу діапазону: '))

# if left2 > right2:
#     left2, right2 = right2, left2

# num1 = left2
# while num1 <= right2:
    
#     if num1 % 3 == 1 and num1 % 5 == 1: print(num1)
    
#     elif num1 % 3 == 0 and num1 % 5 == 0: print("Fizz Buzz")
    
#     elif num1 % 3 == 0: print("Fizz")
    
#     elif num1 % 5 == 0: print("Buzz")
    
#     else:
#         print(num1)

#     num1 += 1







# start = int(input("Введи початок діапазону: "))
# end = int(input("Введи кінець діапазону: "))
# step = int(input("Введи крок: "))

# num1 = input("Порядок (1 - зростаючий, 2 - спадаючий): ")
# if start > end:
#     start, end = end,start


# if num1 == "1":
#     num = start
#     while num <= end:
#         print(num)
#         num += step


# elif num1 == "2":
#     num = end
#     while num >= start:
#         print(num)
#         num -= step

# else:
#     print("Помилка: невірний порядок!")





# num1 = int(input("Введи перше число: "))
# num2 = int(input("Введи друге число: "))


# if num1 > num2:
#     num1, num2 = num2, num1

# product = 1
# found = 0
# num3 = num1

# while num3 <= num2:
#     if num3 % 4 == 0 and num3 % 6 != 0:
#         product *= num3
#         found = 1
#     num3 += 1

# if found:
#     print("Добуток чисел =", product)
# else:
#     print("Немає чисел, що діляться на 4 і не діляться на 6")






# num1 = int(input("Введи число: "))
# num2 = int(input("Введи степінь: "))

# result = 1
# num3 = 0

# while num3 < num2:
#     result *= num1
#     num3 += 1

# print("Результат:", result)




   
width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
symbol = input("Введите символ для рисования: ")

# Рисуем фигуру
for i in range(height):          # идём по строкам
    for j in range(width):       # идём по колонкам
        print(symbol, end=' ')   # печатаем символ с пробелом и остаёмся на той же строке
    print()                      # переходим на следующую строку
