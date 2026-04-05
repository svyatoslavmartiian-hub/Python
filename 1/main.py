from character import *
from enemies import *

grob = Globlin("Grob", 10, 30)
dracula = Vampire("Dracula", 12, 40)


boris = Fighter("Boris", 15, 50)
anna = Healer("Anna", 7, 35)


print("--- Stats before fight ---")
print(grob, dracula, boris, anna, sep="\n")


grob.attack(boris)
dracula.attack(boris)


boris.attack(dracula)
anna.heal(boris)


grob.attack(anna)
dracula.attack(anna)


print("--- Stats before fight ---")

print(grob, dracula, boris, anna, sep="\n")


