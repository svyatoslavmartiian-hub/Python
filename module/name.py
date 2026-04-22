import random

name = input("Введіть базове ім'я (наприклад, svyatoslav): ")

digital_name = name + str(random.randint(100, 9999))

punctuation = ["_", ".", "-"]
sep = random.choice(punctuation)

letters = "abcdefghijklmnopqrstuvwxyz"
rand_letters = random.choice(letters) + random.choice(letters) + random.choice(letters)

letter_name = name + sep + rand_letters

cap_name = name.capitalize()

prefixes = ["Pro", "Super", "Ultra"]
pref = random.choice(prefixes)

nums = str(random.randint(10, 99))

elite_list = list(pref + cap_name + nums)
random.shuffle(elite_list)
elite_name = "".join(elite_list)

print("\n" + "="*30)
print(" ВАРІАНТИ НІКНЕЙМІВ:")
print("="*30)
print(f"1. Цифровий: {digital_name}")
print(f"2. Літерний: {letter_name}")
print(f"3. Елітний:  {elite_name}")
print("="*30)