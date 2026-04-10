def encrypt_text():
    f = open("data.txt", "r", encoding="utf-8")
    text = f.read()
    f.close()

    result = ""
    for char in text:
        if char.isalpha(): 
            
            next_char = chr(ord(char) + 1)
            
            
            if char == 'z': next_char = 'a'
            if char == 'Z': next_char = 'A'
            if char == 'a': next_char = 'b'
            if char == 'A': next_char = 'B'
            if char == 'l': next_char = 'm'
            if char == 'L': next_char = 'M'
            
            result += next_char
        else:
            result += char 

    out = open("encrypted.txt", "w", encoding="utf-8")
    out.write(result)
    out.close()
    print("Шифрування завершено. Результат у encrypted.txt")

if __name__ == "__main__":
    encrypt_text()