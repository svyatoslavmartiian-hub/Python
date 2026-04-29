# num1 = int(input("Ведіть перше число: "))
# num2 = int(input("Ведіть друге число: "))
# print(f"{num1 + num2}")
# print(f"{num1 - num2}")

# print(f"{num1 * num2}")

# 2

# num1 = int(input("Ведіть перше число: "))
# num2 = int(input("Ведіть друге число: "))
# print(f"{num2} відсотків від {num1} = {num1 / 100 * num2}")


# 3

# num1 = int(input("Ведіть ширину: "))
# num2 = int(input("Ведіть висоту: "))

# print(f"Площа прямокутника дорівнює {num1 * num2}")

# 4

# num1 = int(input("Ведіть довжину сторони "))
# print(f"Периметр квадрата = {num1 * 4}")

# 5

# num1 = float(input("Ведіть довжину в М "))
# print(f"Довжина в сантиметрах = {num1 * 100}")

# 6

# num = int(input("Ведіть кількість літрів "))
# print(f"Потрібно {num * 4} літрів ")

# 1


# input_data = input("Ведіть чілі числа через пробіл: ")
# numbers = [int(x) for x in input_data.split()]

# if len(numbers) > 0:

#     max_num = numbers[0]
#     min_num = numbers[0]
#     events = 0
#     for i in numbers: 
#         if i > max_num:
#              max_num = i


#         if i <min_num:
#             min_num = i


#         if i % 2 == 0:
#             events += 1


# print(f"Максимальне число: {max_num} Найменьше число {min_num} Середнє {events}")


# input_data = input("Ведіть чілі числа через пробіл: ")
# nums = int(input("Ведіть число: "))
# numbers = [int(x) for x in input_data.split()]

# print(numbers.count(nums))


# input_data = input("Ведіть чілі числа через пробіл: ")
# numbers = [int(x) for x in input_data.split()]

# total_sum = 0
# for i in numbers: 
#     if i > 0:
#         total_sum += i

# print(total_sum)


input_data = input("Ведіть чілі числа через пробіл: ")
numbers = [int(x) for x in input_data.split()]

index = 0
events_index = []
for i in numbers: 
    if i % 2 ==0:
        index = numbers.index(i)
        events_index

print(index)