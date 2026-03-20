# def show_quote():
#     print('"Don\'t let the noise of others\' opinions')
#     print('    drown out your own inner voice."')
#     print(' ' * 7 + 'Steve Jobs')

# show_quote()








# def odd_numbers():
#     a = int(input("Введіть перше число: "))
#     b = int(input("Введіть друге число: "))

#     if a > b:
#         a, b = b, a

#     i = a + 1
#     while i < b:
#         if i % 2 != 0:
#             print(i, end=" ")
#         i += 1

# odd_numbers()









# def draw_line(length, direction, symbol):
    
#     if direction.lower() == "горизонтальна":
#         print(symbol * length)
#     elif direction.lower() == "вертикальна":
#         for _ in range(length):
#             print(symbol)
#     else:
#         print("Невідомий напрямок. Введіть 'горизонтальна' або 'вертикальна'.")

# length = int(input("Введіть довжину лінії: "))
# direction = input("Введіть напрямок лінії (горизонтальна/вертикальна): ")
# symbol = input("Введіть символ для лінії: ")

# draw_line(length, direction, symbol)







def max_f(a, b, c, d):
    return max(a, b, c, d)

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))

максимум = max_f(num1, num2, num3, num4)
print("Найбільше число:", максимум)