# nums = input("Введіть числа через пробіл: ")

# nums_list = [int(x) for x in nums.split()]

# unique_nums = set(nums_list)

# print("Унікальні числа:", unique_nums)



# import random

# set1 = set(random.randint(1, 20) for i in range(10))
# set2 = set(random.randint(1, 20) for i in range(10))

# print("Множина 1:", set1)
# print("Множина 2:", set2)

# common = set1 & set2
# print("Спільні елементи:", common)

# difference = set1 - set2
# print("Різниця (set1 - set2):", difference)

# union = set1 | set2
# print("Об’єднання:", union)



word1 = input("Введіть перше слово: ").lower()
word2 = input("Введіть друге слово: ").lower()

if set(word1) == set(word2):
    print("Це анаграми.")
else:
    print("Це не анаграми.")