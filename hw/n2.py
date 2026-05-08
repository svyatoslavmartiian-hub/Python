def encrypt_text(text):
    encrypted_result = ""
    for char in text:
        if char.isalpha():
            start_code = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start_code + 1) % 26 + start_code)
            encrypted_result += shifted_char
        else:
            encrypted_result += char
    return encrypted_result

def encrypt_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        encrypted_content = encrypt_text(original_content)
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
            
        print("Шифрування завершено успішно.")
    except FileNotFoundError:
        print("Помилка: Вхідний файл не знайдено.")

encrypt_file('data.txt', 'encrypted.txt')