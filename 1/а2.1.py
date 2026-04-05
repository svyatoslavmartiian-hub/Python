def show_text():
    print('"Don\'t compare yourself with anyone in this world..."')
    print('\tif you do so, you are insulting yourself.')
    print('\t\tBill Gates')

show_text()


def even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)

even_numbers(2, 10)


def print_square(size, char, filled):
    for i in range(size):
        if filled:
            print(char * size)
        else:
            if i == 0 or i == size - 1:
                print(char * size)
            else:
                print(char + ' ' * (size - 2) + char)

print_square(5, '*', True)
print_square(5, '#', False)


def count_digits(number):
    number = abs(number)
    count = 0
    if number == 0:
        return 1
    while number > 0:
        number //= 10
        count += 1
    return count

print(count_digits(3456))
print(count_digits(-789))
print(count_digits(0))


def is_palindrome(number):
    number_str = str(abs(number))
    return number_str == number_str[::-1]

print(is_palindrome(123321))  
print(is_palindrome(546645))  
print(is_palindrome(421987))  
print(is_palindrome(-121))