# contacts = {
#     "Антон" : "034987594373",
#     "Анастасія" : "438648362790",
#     "Сергій" : "7938459435789"
# }

# print(contacts["Антон"])
# contacts["Анастасія"] = "345678908434"
# print(contacts["Анастасія"])
# contacts["Кирило"] = "23456776654509"
# print(contacts)


# contacts.update("Катя" : " 345678900998")
# contacts.update([])
# print(contacts)

# contacts.pop("Антон")
# print(contacts)
# contacts.popitem()
# print(contacts)
# contacts.clear()
# print(contacts)


#  new_dictionary = dict()
# new_dictionary = {
#     "key" : "value",
#     10: 12.3
# }

# print(new_dictionary)
# print(type(new_dictionary))
# my_set = set()
# my_set = set(['apple', 'orange', 'cherry'])

# my_set = {'apple', 'orange', 'cherry', 'mango'}
# my_set2 = {'mango', 'pepper', 'apple', 'kiwi'}

# frozen_fruits = frozenset(my_set | my_set2)
# print(', '.join(frozen_fruits))
# print(type(frozen_fruits))
# frozen_fruits.add()
# frozen_fruits.update()
# frozen_fruits.remove()

# my_set.symmetric_difference_update(my_set2)
# print(my_set)

# sym_difference = my_set.symmetric_difference(my_set2)
# sym_difference = my_set ^ my_set2
# print(sym_difference)

# my_set.difference_update(my_set2)
# print(my_set)

# difference = my_set.difference(my_set2)
# difference = my_set - my_set2
# print(difference)

# my_set.intersection_update(my_set2)
# print(my_set)

# intersect = my_set.intersection(my_set2)
# intersect = my_set & my_set2
# print(intersect)

# union = my_set.union(my_set2)
# union = my_set | my_set2
# print(union)

# print(', '.join(my_set))
# my_set.add('banana')
# print(', '.join(my_set))
# my_set.update(['mango', 'kiwi'])
# print(', '.join(my_set))

# my_set.remove('apple')
# print(', '.join(my_set))
# my_set.discard('banana')
# print(', '.join(my_set))
# my_set.pop()
# print(', '.join(my_set))
# my_set.clear()
# print(', '.join(my_set))


# print('apple' in my_set)
# print('banana' not in my_set)

# print(my_set[0])

# print(my_set)
# print(type(my_set))

# print(len(my_set))

# new_set = {True, 1, 0, False}

# print(new_set)

# my_list = ['apple', 'cherry', 'orange']

# for item in my_set:
#     print(item)


# counter = 0
# while counter < len(my_list):
#     print(my_set[counter])
#     counter += 1