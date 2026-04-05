# Завдання 1       

number1 = int(input("Ведіть число:"))

if number1 % 2 == 0:
    print("Even number")
else:
       print("Odd number")
       
# Завдання 2      


number2 = int(input("Ведіть число:"))

if number1 % 7 == 0:
    print("Number is multiple 7")
else:
       print("Number is not multiple 7")
# Завдання 3       

number3 = int(input("Ведіть перше число:"))
number4 = int(input("Ведіть друге число:"))
if number3 > number4:
      print(f"Найбільше число: {number3}")
else:
      print(f"Найбільше число: {number4}")
# Завдання 4
number5 = int(input("Ведіть перше число:"))
number6 = int(input("Ведіть друге число:"))
if number5 < number6:
      print(f"Найменше число: {number5}")
else:
      print(f"Найменше число: {number6}")

# Завдання 5

USD = float(input("Ведіть суму в доларах "))
currency = str(input("Ведіть обрану валюту(євро (EUR), фунти (GBP) або гривні (UAH))"))
if currency == "EUR":
      print(f"Сумма в євро дорівнює: {USD * 0.86}")
elif currency == "GBP":
      print(f"Сумма в фунтах дорівнює: {USD * 0.75}")
elif currency == "UAN":
      print(f"Сумма в гривнях дорівнює: {USD * 43.15}")
#Завдання 6 

number7 = float(input("Ведіть час у секундах "))
number8 = str(input("Оберіть одиницю вимірювання часу (секунда(A), хвилина (B) або година (C))"))
if number8 == "A":
      print(f"Залишок часу до опівночі в секундах {86400 - number7}")
elif number8 == "B":
      print(f"Залишок часу до опівночі в хвилинах {(86400 - number7) / 60}")
elif number8 == "C":
      print(f"Залишок часу до опівночі в хвилинах {(86400 - number7) / 60 / 60}")

#Завдання 7
PI = 3.14
number9 = float(input("Ведіть діаметр кола "))
text = str(input("Оберіть що порахувати (площу(A), периметр (B))"))
if text == "A":
      print(f"Площа кола дорівнює {PI * (number9 * number9)}")
elif text == "B":
      print(f"Периметр кола дорівнює {PI * number9}")
#Завдання 8
number10 = float(input("Ведіть розмір файлу "))
number11 = float(input("Ведіть швидкість інтернету" ))
text2 = str(input("Оберіть одиницю вимірювання часу (секунда(A), хвилина(B) або годинa(C) "))
if text2 == "A":
      print(f"Ваш файл завантажиться через {(number10 * 8589934592) / number11} секунд")
elif text2 == "B": 
      print(f"Ваш файл завантажиться через {(number10 * 8589934592) / number11 / 60} хвилин")
elif text2 == "C": 
     print(f"Ваш файл завантажиться через {(number10 * 8589934592) / number11 / 60 / 60} годин")
     
#Завдання 9 

number12 = float(input("Ведіть кількість годин "))
if number12 >= 0 and number12 < 6:
    print("Good Night")
elif number12 >= 6 and number12 < 13:
      print("Good Morning")
elif number12 >=13 and number12 < 17:
      print("Good Day")
elif number12 >=17 and number12 < 0:
      print("Good Evening")

#Завдання 10

number13 = float(input("Ведіть поточну температуру "))
if number13 < -10:
    print("Дуже холодно")
elif number12 >= -10 and number12 < 0:
      print("Холодно")
elif number12 >=0 and number12 < 15:
      print("Прохолодно")
elif number12 >=15 and number13 < 25:
      print("Тепло")
elif number13 > 25:
      print("Спекотно")