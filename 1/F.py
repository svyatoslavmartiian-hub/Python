# Завдання 1
def show_quote():
    print('"Don\'t let the noise of others opinions')
    print('\tdrown out your own inner voice."')
    print('\t\tSteve Jobs')


# Завдання 2
def odd_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


# Завдання 3
def draw_line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for _ in range(length):
            print(symbol)
    else:
        print("Невірний напрямок")


# Завдання 4
def max_of_four(a, b, c, d):
    return max(a, b, c, d)


# Завдання 5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Завдання 6
def is_lucky(n):
    s = str(n)
    if len(s) != 6:
        return False
    first = int(s[0]) + int(s[1]) + int(s[2])
    second = int(s[3]) + int(s[4]) + int(s[5])
    return first == second

