#78.right triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    print("*" * i)

#79.inverted right triangle

n = int(input("enter n :"))
for i in range(n, 0, -1):
    print("*" * i)

#80.right aligned triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

#81.inverted right aligned triangle

n = int(input("enter n :"))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

#82.pyramid

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#83.inverted pyramid

n = int(input("enter n :"))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#84.diamond

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#85.hollow rectangle

rows = int(input("enter rows :"))
cols = int(input("enter columns :"))
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#86.hollow right triangle

n = int(input("enter n :"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#87.sandglass

n = int(input("enter n :"))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
