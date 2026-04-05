def copy_file():
    try:
        with open('data.txt', 'r', encoding='utf-8') as source:
            content = source.read()
        
        with open('backup.txt', 'w', encoding='utf-8') as destination:
            destination.write(content)
        
        print("Файл успішно скопійовано!")
    except FileNotFoundError:
        print("Помилка: файл data.txt не знайдено.")

copy_file()