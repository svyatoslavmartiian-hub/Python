# 1
# with open('data.txt', 'r', encoding='utf-8') as f_in:
#     content = f_in.read()

# with open('backup.txt', 'w', encoding='utf-8') as f_out:
#     f_out.write(content)

# print("Файл успішно скопійовано.")


# 3
# def shift_char(char):
#     if 'a' <= char <= 'z':
#         return 'a' if char == 'z' else chr(ord(char) + 1)
#     elif 'A' <= char <= 'Z':
#         return 'A' if char == 'Z' else chr(ord(char) + 1)
#     return char

# with open('data.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# encrypted_text = "".join(shift_char(c) for c in text)

# with open('encrypted.txt', 'w', encoding='utf-8') as f:
#     f.write(encrypted_text)

# print("Текст зашифровано та збережено в encrypted.txt.")



# 3
# def show_menu():
#     print("\n--- Меню ---")
#     print("1. Додати новий альбом")
#     print("2. Переглянути всю колекцію")
#     print("3. Пошук альбомів за виконавцем")
#     print("4. Видалити альбом")
#     print("5. Вихід")

# def add_album():
#     title = input("Назва альбому: ")
#     artist = input("Виконавець: ")
#     year = input("Рік випуску: ")
#     with open('music_collection.txt', 'a', encoding='utf-8') as f:
#         f.write(f"{title};{artist};{year}\n")
#     print("Альбом додано!")

# def view_all():
#     try:
#         with open('music_collection.txt', 'r', encoding='utf-8') as f:
#             lines = f.readlines()
#             if not lines:
#                 print("Колекція порожня.")
#                 return
#             for line in lines:
#                 title, artist, year = line.strip().split(';')
#                 print(f"Альбом: {title} | Виконавець: {artist} | Рік: {year}")
#     except FileNotFoundError:
#         print("Файл колекції ще не створено.")

# def search_by_artist():
#     search_name = input("Введіть ім'я виконавця: ").lower()
#     found = False
#     try:
#         with open('music_collection.txt', 'r', encoding='utf-8') as f:
#             for line in f:
#                 title, artist, year = line.strip().split(';')
#                 if search_name in artist.lower():
#                     print(f"Знайдено: {title} ({year})")
#                     found = True
#         if not found:
#             print("Альбомів цього виконавця не знайдено.")
#     except FileNotFoundError:
#         print("Колекція порожня.")

# def delete_album():
#     target_title = input("Введіть назву альбому для видалення: ").lower()
#     updated_list = []
#     deleted = False
#     try:
#         with open('music_collection.txt', 'r', encoding='utf-8') as f:
#             for line in f:
#                 title, artist, year = line.strip().split(';')
#                 if title.lower() != target_title:
#                     updated_list.append(line)
#                 else:
#                     deleted = True
        
#         with open('music_collection.txt', 'w', encoding='utf-8') as f:
#             f.writelines(updated_list)
        
#         if deleted:
#             print("Альбом видалено.")
#         else:
#             print("Альбом не знайдено.")
#     except FileNotFoundError:
#         print("Колекція порожня.")

# while True:
#     show_menu()
#     choice = input("Оберіть дію: ")
#     if choice == '1':
#         add_album()
#     elif choice == '2':
#         view_all()
#     elif choice == '3':
#         search_by_artist()
#     elif choice == '4':
#         delete_album()
#     elif choice == '5':
#         print("До побачення!")
#         break
#     else:
#         print("Невірний вибір.")