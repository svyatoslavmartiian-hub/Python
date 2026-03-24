def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("Завдання 1:")
print("2^5 =", power(2, 5))


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def days_since_0(day, month, year):
    days = day
    for y in range(1, year):
        days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        days += days_in_month(m, year)
    return days

def date_difference(day1, month1, year1, day2, month2, year2):
    return abs(days_since_0(day2, month2, year2) - days_since_0(day1, month1, year1))

print("\nЗавдання 2:")
print("Різниця днів між 01.01.2020 і 01.01.2021 =", date_difference(1, 1, 2020, 1, 1, 2021))


import random

numbers = [random.randint(1, 100) for _ in range(100)]

def min_sum_position(lst, start=0, min_pos=0, min_sum=float('inf')):
    if start > len(lst) - 10:
        return min_pos
    current_sum = sum(lst[start:start+10])
    if current_sum < min_sum:
        min_sum = current_sum
        min_pos = start
    return min_sum_position(lst, start + 1, min_pos, min_sum)

pos = min_sum_position(numbers)
print("\nЗавдання 3:")
print("Початкова позиція мінімальної суми 10 чисел:", pos)
print("Мінімальна сума:", sum(numbers[pos:pos+10]))
print("Сама послідовність:", numbers[pos:pos+10])