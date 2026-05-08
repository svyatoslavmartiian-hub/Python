import os

DB_FILE = "music_collection.txt"

def add_album():
    title = input("Введіть назву альбому: ")
    artist = input("Введіть виконавця: ")
    year = input("Введіть рік випуску: ")
    
    with open(DB_FILE, "a", encoding="utf-8") as file:
        file.write(f"{title}|{artist}|{year}\n")
    print("Альбом додано!")

def view_collection():
    if not os.path.exists(DB_FILE):
        print("Колекція порожня.")
        return
    
    print("\n--- Ваша колекція ---")
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            title, artist, year = line.strip().split("|")
            print(f"Альбом: {title} | Виконавець: {artist} | Рік: {year}")

def search_by_artist():
    search_name = input("Введіть ім'я виконавця для пошуку: ").lower()
    found = False
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as file:
            for line in file:
                title, artist, year = line.strip().split("|")
                if search_name in artist.lower():
                    print(f"Знайдено: {title} ({year})")
                    found = True
    
    if not found:
        print("Альбомів цього виконавця не знайдено.")

def delete_album():
    target_title = input("Введіть назву альбому, який треба видалити: ").lower()
    if not os.path.exists(DB_FILE):
        return

    albums = []
    deleted = False
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            title, artist, year = line.strip().split("|")
            if title.lower() != target_title:
                albums.append(line)
            else:
                deleted = True
    
    if deleted:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            file.writelines(albums)
        print("Альбом видалено.")
    else:
        print("Альбом не знайдено.")

def main_menu():
    while True:
        print("\n--- Меню керування музикою ---")
        print("1. Додати новий альбом")
        print("2. Переглянути всю колекцію")
        print("3. Пошук за виконавцем")
        print("4. Видалити альбом")
        print("5. Вихід")
        
        choice = input("Оберіть дію (1-5): ")
        
        if choice == "1": add_album()
        elif choice == "2": view_collection()
        elif choice == "3": search_by_artist()
        elif choice == "4": delete_album()
        elif choice == "5": 
            print("Бувайте!")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()