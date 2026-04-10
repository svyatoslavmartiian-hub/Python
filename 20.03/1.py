original = open("data.txt", "r", encoding="utf-8")
content = original.read()
original.close()

backup = open("backup.txt", "w", encoding="utf-8")
backup.write(content)
backup.close()

print("Файл успішно скопійовано у backup.txt")