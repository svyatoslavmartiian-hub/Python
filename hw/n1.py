def copy_file_content(source_filename, destination_filename):
    try:
        with open(source_filename, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        with open(destination_filename, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)
            
        print(f"Файл успішно скопійовано з {source_filename} у {destination_filename}")
    except FileNotFoundError:
        print(f"Помилка: Файл {source_filename} не знайдено.")

copy_file_content('data.txt', 'backup.txt')