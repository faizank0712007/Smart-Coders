#103.butterfly

n = int(input("enter n :"))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

#104.hollow diamond

n = int(input("enter n :"))
size = 2 * n
for i in range(size):
    for j in range(size):
        distance = abs(i - n) + abs(j - n)
        if distance == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#105.number diamond

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

#106.zigzag

rows = 3
n = int(input("enter length :"))
matrix = [[0] * n for i in range(rows)]
row = 0
going_down = True
for col in range(n):
    matrix[row][col] = 1
    if going_down:
        row = row + 1
        if row == rows:
            row = rows - 2
            going_down = False
    else:
        row = row - 1
        if row < 0:
            row = 1
            going_down = True
for i in matrix:
    print(" ".join("*" if j else " " for j in i))

#107.spiral number matrix

n = 4
matrix = [[0] * n for i in range(n)]
top = 0
bottom = n - 1
left = 0
right = n - 1
num = 1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = num
        num = num + 1
    top = top + 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num = num + 1
    right = right - 1
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num
        num = num + 1
    bottom = bottom - 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num = num + 1
    left = left + 1
for row in matrix:
    print(*row)

#108.right arrow

n = int(input("enter n :"))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * i)

#109.x pattern

n = int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if j == i or j == n - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#110.plus pattern

n = int(input("enter odd n :"))
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#111.heart pattern

for y in range(15, -15, -1):
    yy = y / 10
    row = ""
    for x in range(-15, 16):
        xx = x / 10
        value = (xx ** 2 + yy ** 2 - 1) ** 3 - (xx ** 2) * (yy ** 3)
        if value <= 0:
            row = row + "*"
        else:
            row = row + " "
    print(row)

#112.square diagonals

n = int(input("enter n :"))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
