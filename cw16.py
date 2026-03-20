# contacts = {}
# while True:
#     print("--- КОНТАКТНА КНИЖКА ---")
#     print("1 - Додати контакт")
#     print("2 - Видалити контакт")
#     print("3 - Змінити контакт")
#     print("4 - Показати всі контакти")
#     print("0 - Вихід")
#     choice = int(input("Виберіть дію: "))
#     if choice == 1:
#         name = input("Ведіть ім'я контакта: ")
#         phone = input("Ведіть номер телефона контакта: ")
#         contacts[name] = phone
#         print("Контакт додано")
#     elif choice == 2: 
#         name_1 = input("Ведіть ім'я контакта: ")
#         if name_1 in contacts:
#             contacts.pop(name_1)
#             print("Контакт видаленно")
#         else:
#             print("Контакт не знайдено")
#     elif choice == 3:
#         name_1 = input("Ведіть ім'я контакта який треба замінити: ")
#         if name_1 in contacts:
#             contacts.pop(name_1)
#             name_2 = input("Ведіть нове ім'я: ")
#             phone = int(input("Ведіть новий номер телефону: "))
#             contacts[name_2] = phone
#             print("Контакт зміненно")
#         else:
#             print("Контакт не знайденно")
#     elif choice == 4:
#         print((contacts))        
#     elif choice == 0:
#         print("Вихід")
#         break    

# ЗАВДАННЯ 2


# text = input("Введіть текст: ")

# text = text.lower()          
# words = text.split()          

# counts = {}                   
# for i in words:
#     if i in counts:
#         counts[i] += 1
#     else:
#         counts[i] = 1


# for i in counts:
#     print(i, "=", counts[i])

# ЗАВДАННЯ 3



# rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
# print(rates)
# gr = int(input("Ведіть суму в гривнях: "))
# rt = input("Ведіть валюту(USD, EUR, PLN): ")
# if rt in rates:
#     gt = gr / rates[rt]
#     print(f"{gr} грн = {gt} {rt}")
# else:
#     print("Невідома валюта")


# Завдання 4




# dictionary = {
#     "cat": "кіт",
#     "dog": "собака",
#     "book": "книга",
#     "car": "машина",
#     "hello": "привіт",
#     "apple": "яблуко",
#     "orange": "апельсин",
#     "pen": "ручка",
#     "ukraine": "україна",
#     "nice": "гарний"
# }

# word = input("Введіть слово англійською: ").lower()

# if word in dictionary:
#     print("Переклад:", dictionary[word])
# else:
#     print("Слово не знайдено")