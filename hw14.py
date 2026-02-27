# numbers = input("Введіть числа через пробіл: ")
# N = int(input("Введіть N: "))

# numbers = numbers.split()
# numbers = [int(x) for x in numbers]

# length = len(numbers)

# N = N % length

# shifted = numbers[-N:] + numbers[:-N]

# print("Зсунутий список:", shifted)






import random

list1 = [random.randint(1, 10) for i in range(5)]
list2 = [random.randint(1, 10) for i in range(5)]

print("Список 1:", list1)
print("Список 2:", list2)

list_all = list1 + list2
print("Всі елементи обох списків:", list_all)

list_unique = list(set(list1 + list2))
print("Унікальні елементи обох списків:", list_unique)

list_common = list(set(list1).intersection(set(list2)))
print("Спільні елементи:", list_common)

list_diff = list(set(list1).symmetric_difference(set(list2)))
print("Унікальні елементи кожного списку:", list_diff)

list_min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Мінімальні та максимальні значення кожного списку:", list_min_max)