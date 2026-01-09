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
number8 = str(input("Ведіть скільки залишилось часу в (секундах(A), хвилинах (B) або годинах (C))"))
if number8 == "A":
      print(f"Залишок часу до опівночі в секундах {86400 - number7}")
elif number8 == "B":
      print(f"Залишок часу до опівночі в хвилинах {(86400 - number7) / 60}")
elif number8 == "C":
      print(f"Залишок часу до опівночі в хвилинах {(86400 - number7) / 60 / 60}")

#Завдання 7

      



