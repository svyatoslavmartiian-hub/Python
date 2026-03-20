# '''
# Є список цін на товари. Необхідно розрахувати нові ціни зі знижкою у 20%, але тільки для товарів, дорожчих за 100.
# '''

# def get_discounted_prices(prices: list):
#     discounted_prices = []

#     for price in prices:
#         if price > 100:
#             new_price = price * 0.8
#             discounted_prices.append(new_price)

#     return discounted_prices


# original_prices = [50, 120, 80, 200, 300]
# result = get_discounted_prices(original_prices)
# print(result)


# def some_func():
#     print('Hello')


# func_var = some_func
# print(type(func_var))
# func_var()

# def some_func_with_callback(callback):
#     print('function that calls another function')
#     callback()


# def print_greet():
#     print('Greetings!')
    

# some_func_with_callback(some_func)
# some_func_with_callback(print_greet)


# operations = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a / b if b != 0 else 'Zero division'
# }

# num1 = float(input('Enter first num: '))
# num2 = float(input('Enter second number: '))
# action = input('Enter sign (+, -, *)')

# if action in operations:
#     print(operations[action](num1, num2))
# else:
#     print('Incorrect sign!')

# tax_rate = 0.2

# def calc_tax_impure(amount):
#     return amount * tax_rate


# def calc_tax_pure(amount, tax_rate):
#     return amount * tax_rate


# print(calc_tax_pure(10, 0.3))

# my_cart = ['apple', 'banana']
# # cart = my_cart

# def add_product_impure(cart, product):
#     cart.append(product)
#     return cart


# def add_product_pure(cart: list, product: str) -> list:
#     new_cart = cart.copy()
#     new_cart.append(product)
#     return new_cart

# new_cart = add_product_pure(my_cart, 'orange')
# print(new_cart)
# print(my_cart)

# my_list = [15, 8, 42, 4, 16, 23]

# even = []

# for num in my_list: # імперативний підхід
#     if num % 2 == 0:
#         even.append(num)

# even_numbers = list(filter(lambda a: a % 2 == 0, my_list)) # декларативний

# print(even_numbers)

# original_prices = [50, 120, 80, 200, 300]
# discounted_prices = list(map(lambda a: a * 0.8, filter(lambda a: a > 100, original_prices)))
# print(discounted_prices)