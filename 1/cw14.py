# data = input("Ведіть цілі числа через пробіл: ").split()

# numbers = []
# for x in data:
#     numbers.append(int(x))   

# s = 0
# for x in numbers:
#     s += x

# avg = s / len(numbers)

# print("Сума:", s)
# print("Середнє арифметичне:", avg)







# num1 = input("Ведіть цілі числа через пробіл: ").split()
# num2 = input("Ведіть число: ")

# k = num1.count(num2)
# print(k)






# a = input("Введи числа через пробіл: ").split()

# numbers = []
# for x in a:
#     numbers.append(int(x))

# s = 0
# for x in numbers:
#     if x > 0:     
#         s += x

# print("Сума додатних чисел:", s)



s = input("Введи числа через пробіл: ")
parts = s.split()

nums = []
for x in parts:
    nums.append(int(x))

indexes = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        indexes.append(i)

print("Індекси парних чисел:", indexes)


s = input("Введи числа через пробіл: ")
parts = s.split()

nums = []
for x in parts:
    nums.append(int(x))

unique = []
for x in nums:
    if x not in unique:
        unique.append(x)

print("Унікальні числа:", unique)