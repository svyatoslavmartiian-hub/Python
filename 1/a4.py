def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("Завдання 1:")
print("Найбільший спільний дільник 48 і 18 =", gcd(48, 18))





def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print("\nЗавдання 2:")
num = 123
print(f"Сума цифр числа {num} =", sum_digits(num))





def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])

print("\nЗавдання 3:")
lst = [1, 2, 3, 2, 1]
if is_symmetric(lst):
    print(f"Список {lst} симетричний")
else:
    print(f"Список {lst} не симетричний")