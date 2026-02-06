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






left = int(input('Введіть ліву межу діапазону: '))
right = int(input('Введіть праву межу діапазону: '))
kr = int(input("Ведіть інтервал: "))
intr = str(input("Виберіть у якому порядку вивести числа(1-Спадаючий, 2-Зростаючий): "))

if left > right:
    left, right = right, left

counter = left

countMultiply5 = 0

print("Усі числа діапазону: ")
while counter <= right:
    if intr == 1:
        print(counter, end=' ')
    counter += kr


    


   
