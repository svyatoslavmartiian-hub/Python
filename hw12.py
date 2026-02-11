n = 12 
print("Фігура 1:")

for i in range(n):
    for j in range(n):
        if i <= j and i + j >= n - 1:
            print("*", end=" ")
        elif i >= j and i + j <= n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 2:")

for i in range(n):
    for j in range(n):
        if i >= j and i + j <= n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 3:")


for i in range(n):
    for j in range(n):
        if i <= j and i + j >= n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 4:")


for i in range(n):
    for j in range(n):
        if j <= n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 5:")
 
for i in range(n):
    for j in range(n):
        if j >= n - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 6:")

for i in range(n):
    for j in range(n):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Фігура 7:")


for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 8:")


t = 7
for i in range(t, 0, -1):
    for j in range(t - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

print("Фігура 9:")
  



for i in range(1, t + 1):
    for j in range(t - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
print("Фігура 10:")



for i in range(t, 0, -1):
    for j in range(t - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


for i in range(2, t + 1):
    for j in range(t - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


intt = int(input("Ведіть розмір фігури: "))
intt2 = int(input("Ведіть символ яким намалювати фігури: "))


print("Фігура 1:")

for i in range(intt):
    for j in range(intt):
        if i <= j and i + j >= intt - 1:
            print(intt2, end=" ")
        elif i >= j and i + j <= intt - 1:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 2:")

for i in range(intt):
    for j in range(intt):
        if i >= j and i + j <= intt - 1:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 3:")


for i in range(intt):
    for j in range(intt):
        if i <= j and i + j >= intt - 1:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 4:")


for i in range(intt):
    for j in range(intt):
        if j <= intt - i - 1:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 5:")
 
for i in range(intt):
    for j in range(intt):
        if j >= intt - i + 1:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 6:")

for i in range(intt):
    for j in range(intt):
        if j >= i:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()

print("Фігура 7:")


for i in range(intt):
    for j in range(intt):
        if j <= i:
            print(intt2, end=" ")
        else:
            print(" ", end=" ")
    print()
print("Фігура 8:")


t = 7
for i in range(intt, 0, -1):
    for j in range(intt - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(intt2, end=" ")
    print()

print("Фігура 9:")
  



for i in range(1, intt + 1):
    for j in range(intt - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(intt2, end=" ")
    print()
print("Фігура 10:")



for i in range(intt, 0, -1):
    for j in range(intt - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(intt2, end=" ")
    print()


for i in range(2, intt + 1):
    for j in range(intt - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(intt2, end=" ")
    print()
