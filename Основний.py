# Програмування це - це створення програмного коду, програмного забеспечення.
# 1.Аналіз задачі
# 2.
# 3.Написання коду 
# 4.Тестування та виправлення помилок
# Тип даних - Харакеристика даних, що визначає діапазон значень
# та набір операцій
# ---------------------
# int - цілі числа 
# float - дробові числа
# bool - True // Fаlse
# ---------------------
# str - текст
# range  - генератор послідовності чисел
# type - інформація про інший тип даних.
# NoneType - 	Відсутність значення
# list - Списки


# intType = type(10)
# print(intType.__name__)
# print(type(intType))

# Змінна - іменованна область пам'яті яка зберігає дані які ми можемо використовувати в коді

# Умовні конструкції - це конструкція в мові програмуванні яка дозволяє виконувати розгалуженні алгоритми.

# Розгалужені алгоритми в Python — це алгоритми, в яких виконання програми залежить від певної умови.

# Алгоритм – це чітка, покрокова послідовність дій.

# Цикл  це алгоритмічна структура, що дозволяє виконувати - 

# - одну й ту саму послідовність дій кілька разів.

# Списки — це структури даних, які використовуються для зберігання об'єктів різних типів, які можна змінювати.

# Кортеж - це структури даних, які використовуються для зберігання об'єктів різних типів, які не можна змінювати.

# Колекція - це спеціальний тип об’єкта, який зберігає набір елементів і дозволяє з ними працювати.

# Словники - це колекція, яка зберпігається у виді, ключ - значення.

# Рядок це колекція яка зберігає тільки символи.

# Функції — це іменовані блоки коду, які виконують певну дію та можуть повертати результат.

# Параметр – це характеристика або вхідне значення, яке може змінювати поведінку системи чи алгоритму без зміни самої структури процесу.

# Алгоритм – це чітка, послідовна і кінцева інструкція для виконання завдання або розв’язання проблеми.


# Параметр описує як щось робити, тоді як параметри визначають з якими даними або налаштуваннями це робити.




# collection = list()  # функція конструктор
# collection = []

# print(type(collection)) # <class "list">

# items = [10,12,3, "text", True] # погана практика

# fruits = ["avocado", "apple", "orange", "lemon"]

# print(fruits[0])
# print(fruits[1])
# print(fruits[1:3])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[1:4:2])
# print(fruits[::2])

# print(fruits[-1])
# print(fruits[-1:-3: -2])
# print(fruits[::-1])


# string = "text"
# string[2] = "u"

# print(fruits)
# fruits[1] = 'mango' # apple -> mango
# print(fruits)


# fruits_count = len(fruits)
# print(fruits_count)

# counter = 0
# while counter < len(fruits):
#     print(fruits[counter])
#     counter += 1


# for fruit in fruits:
#     print(fruit)

# names = input("Ведіть список імен через кому: ")
# print(type(names))
# names = names.split()
# print(type(names))
# print(names)
# names = ", ".join(names)
# print(names)
# print(type(names))





# fruits = ['avocado', 'apple', 'orange', 'lemon', 'pear']

# print(', '.join(fruits))

# fruits.append('ananas')
# print(', '.join(fruits))

# fruits.extend(['mandarin', 'grapefruit'])
# print(', '.join(fruits))

# fruits.insert(4, 'mango')
# print(', '.join(fruits))


# fruits_copy = fruits.copy()
# fruits_copy.append('orange')
# print(fruits_copy)
# print(fruits)


# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# list1 = [2,3,4]
# list2 = [5,6,7]

# result = list1 + list2
# print(result)

# print(result * 3)list2d = [ 
#     [1,2,3], 
#     [4,5,6] 
# ]

# print(list2d[0])
# print(list2d[0][1])

# for i in list2d:
#     for j in i:
#         print(j, end=' ')
#     print()

# УРОК  
def print_contacts(contact):
    if contacts[key]["mobile"] != None: print(f"\tмобільний: {contacts[key]{"mobile"}}")
    if contacts[key]["job"] != None: print(f"\tробочий: {contacts[key]["job"]}")

contacts = {
    "Ana":{
        "mobile": "8726343846728",
        "job": "435498597585"
    },
    "Anton STO": {
        "mobile": "29875757933",
        "job": None
    },
    "tunmofiy Korpatu":{
        "mobile": None,
        "job": "29875757933"

    }




}


print("1. Продивитися контакти/n 2. Знайти контакт/n 0.Вийти")
action = input("Оберіть дію: ")


while action != 0:
    match action:
        case "1":
            for key in contacts:
                print(key)
                if contacts[key]["mobile"] != None: print(f"\tмобільний: {contacts[key]{"mobile"}}")
                if contacts[key]["job"] != None: print(f"\tробочий: {contacts[key]["job"]}")
        case "2":
            name = input("Ведіть ім'я: ")
            if name in contacts:



