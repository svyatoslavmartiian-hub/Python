class Book:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors 
        self.year = year

    def __str__(self):
        authors_str = ", ".join(self.authors)
        return f"Книга: {self.title}\nАвтори: {authors_str}\nРік: {self.year}\n"


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def __str__(self):
        return f"Бібліотека: {self.name}\nАдреса: {self.address}\nКниг у наявності: {len(self.books)}"
    def show_all_books(self):
        print(f"\n--- Каталог бібліотеки '{self.name}' ---")
        if not self.books:
            print("Поки що порожньо.")
        else:
            for book in self.books:
                print(book)

    def add_book(self, book):
        self.books.append(book)
        print(f"Система: Книгу '{book.title}' додано успішно.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Система: Книгу '{title}' видалено.")
                return
        print("Система: Такої книги не знайдено.")

    def search_by_title(self, title):
        print(f"\nРезультати пошуку за назвою '{title}':")
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("Нічого не знайдено.")

    def search_by_author(self, author_name):
        print(f"\nРезультати пошуку за автором '{author_name}':")
        found = False
        for book in self.books:
            for author in book.authors:
                if author_name.lower() in author.lower():
                    print(book)
                    found = True
                    break
        if not found:
            print("Книг цього автора не знайдено.")



def main():
    my_library = Library("Книжкова Хата", "вул. Соборна, 5")

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Додати нову книгу")
        print("2. Показати всі книги")
        print("3. Видалити книгу за назвою")
        print("4. Пошук за назвою")
        print("5. Пошук за автором")
        print("6. Інфо про бібліотеку")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        if choice == "1":
            title = input("Назва книги: ")
            authors = input("Автори (через кому): ").split(",")
            authors = [a.strip() for a in authors]
            year = input("Рік видання: ")
            
            new_book = Book(title, authors, year)
            my_library.add_book(new_book)

        elif choice == "2":
            my_library.show_all_books()

        elif choice == "3":
            title = input("Яку книгу видалити: ")
            my_library.remove_book(title)

        elif choice == "4":
            title = input("Введіть назву для пошуку: ")
            my_library.search_by_title(title)

        elif choice == "5":
            author = input("Введіть ім'я автора: ")
            my_library.search_by_author(author)

        elif choice == "6":
            print(my_library)

        elif choice == "0":
            print("Програму завершено!")
            break
        else:
            print("Помилка: спробуйте ще раз.")

if __name__ == "__main__":
    main()