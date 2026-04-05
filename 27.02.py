# 1
# def print_quote():
#     print('"Don\'t let the noise of others\' opinions')
#     print(' drown out your own inner voice."')
#     print('       Steve Jobs')

# print_quote()


# 2
# def show_odd_numbers(a, b):
#     start = min(a, b)
#     end = max(a, b)
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             print(i)

# show_odd_numbers(1, 10)

# 3

# def draw_line(length, direction, symbol):
#     if direction == "horizontal":
#         print(symbol * length)
#     elif direction == "vertical":
#         for i in range(length):
#             print(symbol)

# draw_line(5, "horizontal", "*")
# draw_line(3, "vertical", "|")


# 4
# def get_max(a, b, c, d):
#     maximum = a
#     if b > maximum:
#         maximum = b
#     if c > maximum:
#         maximum = c
#     if d > maximum:
#         maximum = d
#     return maximum

# print(get_max(10, 5, 25, 3))


# 5
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# print(is_prime(7))  
# print(is_prime(10)) 

# 6
# def is_lucky_number(num):
#     s = str(num)
#     if len(s) != 6:
#         return False
    
#     sum1 = int(s[0]) + int(s[1]) + int(s[2])
#     sum2 = int(s[3]) + int(s[4]) + int(s[5])
    
#     if sum1 == sum2:
#         return True
#     else:
#         return False

# print(is_lucky_number(123420))
# print(is_lucky_number(723422)) 