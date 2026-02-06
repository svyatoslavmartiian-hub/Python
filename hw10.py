# num1 = int(input("Ведіть перше число: "))
# num2 = int(input("Ведіть друге число: "))
# num3 = num1
# while num3 <= num2:
#     if num3 % 7 == 0:
#         print(num3)
#     num3 += 1


num1 = int(input("Ведіть перше число"))
num2 = int(input("Ведіть друге число"))
num3 = num1
while num3 <= num2:
    print(num3)
    num3 += 1
num3 = num2
print()
while num3 >= num1:
    print(num3)
    num3 -=1 
num3 = num1
print()
while num3 <= num1:
    if num3 % 7:       
        print(num3)
    num3 +=1 