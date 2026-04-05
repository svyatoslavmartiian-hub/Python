# text = input("Введіть текст: ")

# sentences = text.count('.') + text.count('!') + text.count('?')

# print("Кількість речень:", sentences)




# text = input("Введіть рядок: ")

# n_text = text.replace(" ", "").lower()

# if n_text == n_text[::-1]:
#     print("Це паліндром")
# else:
#     print("Це не паліндром")





# text = input("Введіть текст: ")

# reserved_words = ["if", "else", "for", "while", "def", "class"]

# words = text.split()

# for i in range(len(words)):
#     if words[i].lower() in reserved_words:
#         words[i] = words[i].upper()

# new_text = " ".join(words)

# print("Змінений текст:")
# print(new_text)






# text = input("Введіть рядок: ")
# char1 = input("Введіть перший символ: ")
# char2 = input("Введіть другий символ: ")

# pos1 = text.find(char1)
# pos2 = text.find(char2)

# if pos1 != -1 and pos2 != -1 and pos1 < pos2:
#     new_text = text[:pos1] + text[pos2+1:]
#     print("Результат:", new_text)
# else:
#     print("Неможливо виконати операцію")





# text = input("Введіть текст: ")
# chars = input("Введіть набір символів: ")

# words = text.split()
# result = []

# for word in words:
#     remove = False
#     for ch in chars:
#         if ch in word:
#             remove = True
#             break
#     if remove == False:
#         result.append(word)

# new_text = " ".join(result)

# print("Результат:")
# print(new_text)






text = input("Введіть текст: ")

words = text.split()        
words.reverse()             

new_text = " ".join(words)

print("Зворотний текст:")
print(new_text)