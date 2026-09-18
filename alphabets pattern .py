
#98.alphabet row repeat

n = int(input("enter n :"))
for i in range(n):
    print(chr(65 + i) * (i + 1))

#99.alphabet sequential

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#100.reverse alphabet triangle

n = int(input("enter n :"))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#101.right aligned alphabet

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#102.alphabet pyramid

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()
  
