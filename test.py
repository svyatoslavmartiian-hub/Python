
# 1
# text = str(input("Ведіть текст: "))
# letters = 0
# digits = 0

# for i in text:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits += 1

# print("Кількість букв: ", letters)
# print("Кількість цифр: ", digits)




# 2
# text_2 = str(input("Ведіть текст: "))
# letters_2 = str(input("Ведіть символ для пошуку: "))
# count = 0
# for x in text_2:
#     if x == letters_2:
#         count +=1


# print("Символ", letters_2, "зустрічається", count, "разів")





# 3
# text = input("Введіть рядок: ")

# result = ""
# for i in text:
#     result = i + result

# print(result)

# text = input("Введіть рядок: ")
text_1 = input("Введіть рядок: ")
text_2 = input("Введіть слово для заміни: ")
text_3 = input("Введіть нове слово: ")


result = text_1.replace(text_2, text_3, 1)

print("Результат:", result)


