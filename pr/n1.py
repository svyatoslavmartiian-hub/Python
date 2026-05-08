def save_user_input_to_file():
    user_sentences = [] 
    
    for i in range(3):
        raw_text = input(f"Введіть рядок №{i+1}: ")
        user_sentences.append(raw_text + "\n")
    
    with open("data.txt", "w", encoding="utf-8") as output_file:
        output_file.writelines(user_sentences)

save_user_input_to_file()