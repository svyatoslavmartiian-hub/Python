import os

def menu():
    file_name = "music_collection.txt"

    while True:
        print("\n--- МОЯ МУЗИКА ---")
        print("1. Додати новий альбом")
        print("2. Переглянути всю колекцію")
        print("3. Пошук за виконавцем")
        print("4. Видалити альбом")
        print("5. Вихід")
        
        choice = input("Ваш вибір: ")

        if choice == "1":
            album = input("Назва альбому: ")
            artist = input("Виконавець: ")
            year = input("Рік випуску: ")
            
            f = open(file_name, "a", encoding="utf-8")
            f.write(f"{album}|{artist}|{year}\n")
            f.close()
            print("Альбом додано!")

        elif choice == "2":
            if not os.path.exists(file_name):
                print("Колекція порожня.")
                continue
            f = open(file_name, "r", encoding="utf-8")
            for line in f:
                parts = line.strip().split("|")
                print(f"Альбом: {parts[0]}, Виконавець: {parts[1]}, Рік: {parts[2]}")
            f.close()

        elif choice == "3":
            search_artist = input("Введіть ім'я виконавця: ").lower()
            f = open(file_name, "r", encoding="utf-8")
            found = False
            for line in f:
                parts = line.strip().split("|")
                if parts[1].lower() == search_artist:
                    print(f"Знайдено: {parts[0]} ({parts[2]})")
                    found = True
            if not found:
                print("Альбомів цього виконавця не знайдено.")
            f.close()

        elif choice == "4":
            del_name = input("Введіть назву альбому для видалення: ").lower()
            if not os.path.exists(file_name): return
            
            f = open(file_name, "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            
            new_lines = []
            deleted = False
            for line in lines:
                if line.strip().split("|")[0].lower() != del_name:
                    new_lines.append(line)
                else:
                    deleted = True
            
            if deleted:
                f = open(file_name, "w", encoding="utf-8")
                f.writelines(new_lines)
                f.close()
                print("Альбом видалено.")
            else:
                print("Альбом не знайдено.")

        elif choice == "5":
            print("Вихід!")
            break

if __name__ == "__main__":
    menu()