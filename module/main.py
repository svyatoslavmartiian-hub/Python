import console

menu_items = ["Нова гра", "Завантажити збереження", "Вихід"]

console.draw_header("СУПЕР ГРА 2026")
console.draw_menu(menu_items)

print("=" * 40)
user_choice = input("Ваш вибір: ")

if user_choice == "1":
    print("\nЗапуск нової гри...")
elif user_choice == "2":
    print("\nЗавантаження даних...")
elif user_choice == "3":
    print("\nДо зустрічі!")
else:
    console.draw_warning("ПОМИЛКА")