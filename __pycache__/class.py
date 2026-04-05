class Animal:
    def make_sound(self):
        print("animal makes some sound")
animal = Animal()
animal.make_sound()
animal(animal.type)
print(type(animal))


class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtruct(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 == 0:raise ZeroDivisionError()
        return num1 / num2
    
calc = Calculator
