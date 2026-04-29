# 1

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        try:
            grade_int = int(grade)
            self.grades.append(grade_int)
            print(f"--- Оцінку {grade_int} успішно додано! ---")
        except ValueError:
            print("--- Помилка: введіть числове значення для оцінки ---")

    def show_grades(self):
        if not self.grades:
            print(f"--- У студента {self.name} ще немає жодної оцінки ---")
        else:
            print(f"--- Оцінки студента {self.name}: {self.grades} ---")

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, вік: {self.age}"


class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def display_info(self):
        print(f"\nІнформація про авто:\nБренд: {self.brand}\nМодель: {self.model}\nШвидкість: {self.speed}\nРік: {self.year}")

    def __str__(self):
        return f"Авто: {self.brand} {self.model} ({self.year})"


def menu():
    student = None
    car = None

    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Створити студента")
        print("2. Додати оцінку")
        print("3. Вивести всі оцінки")
        print("4. Вивести інформацію про студента (str)")
        print("-" * 20)
        print("5. Створити автомобіль")
        print("6. Вивести інформацію про авто")
        print("7. Вивести коротку інформацію про авто (str)")
        print("0. Вихід")
        
        choice = input("\nОберіть пункт: ")

        if choice == "1":
            n = input("Ім'я: ")
            s = input("Прізвище: ")
            a = input("Вік: ")
            student = Student(n, s, a)
            print("--- Студента створено! ---")

        elif choice == "2":
            if student:
                g = input("Введіть оцінку: ")
                student.add_grade(g)
            else:
                print("!!! Помилка: Спочатку створіть студента (пункт 1) !!!")

        elif choice == "3":
            if student:
                student.show_grades()
            else:
                print("!!! Помилка: Студент не створений. Натисніть 1 !!!")

        elif choice == "4":
            if student:
                print(student)
            else:
                print("!!! Студент не створений !!!")

        elif choice == "5":
            b = input("Бренд: ")
            m = input("Модель: ")
            sp = input("Швидкість: ")
            y = input("Рік: ")
            car = Car(b, m, sp, y)
            print("--- Авто створено! ---")

        elif choice == "6":
            if car:
                car.display_info()
            else:
                print("!!! Авто не створено. Натисніть 5 !!!")

        elif choice == "7":
            if car:
                print(car)
            else:
                print("!!! Авто не створено !!!")

        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()

# 2

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = float(radius)

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimetr(self):
#         return 2 * math.pi * self.radius

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = float(a)
#         self.b = float(b)

#     def area(self):
#         return self.a * self.b

#     def perimetr(self):
#         return 2 * (self.a + self.b)

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = float(a)
#         self.b = float(b)
#         self.c = float(c)

#     def perimetr(self):
#         return self.a + self.b + self.c

#     def area(self):
#         p = self.perimetr() / 2
#         d = p * (p - self.a) * (p - self.b) * (p - self.c)
#         if d < 0:
#             return 0
#         return math.sqrt(d)

# def main():
#     while True:
#         print("\n=== МЕНЮ ГЕОМЕТРИЧНИХ ФІГУР ===", flush=True)
#         print("1. Коло (Circle)")
#         print("2. Прямокутник (Rectangle)")
#         print("3. Трикутник (Triangle)")
#         print("0. Вихід")
        
#         choice = input("\nОберіть фігуру: ")

#         if choice == "1":
#             r = input("Введіть радіус: ")
#             shape = Circle(r)
#             print(f"\nРезультат для Кола:")
#             print(f"Площа: {shape.area():.2f}")
#             print(f"Периметр: {shape.perimetr():.2f}", flush=True)

#         elif choice == "2":
#             a = input("Сторона A: ")
#             b = input("Сторона B: ")
#             shape = Rectangle(a, b)
#             print(f"\nРезультат для Прямокутника:")
#             print(f"Площа: {shape.area():.2f}")
#             print(f"Периметр: {shape.perimetr():.2f}", flush=True)

#         elif choice == "3":
#             a = input("Сторона A: ")
#             b = input("Сторона B: ")
#             c = input("Сторона C: ")
#             shape = Triangle(a, b, c)
#             area_val = shape.area()
#             if area_val == 0:
#                 print("\nПомилка: трикутник з такими сторонами не існує!")
#             else:
#                 print(f"\nРезультат для Трикутника:")
#                 print(f"Площа: {area_val:.2f}")
#                 print(f"Периметр: {shape.perimetr():.2f}", flush=True)

#         elif choice == "0":
#             print("Вихід...")
#             break
#         else:
#             print("Невірний вибір!")

# if __name__ == "__main__":
#     main()