#43.print 1 to n
n = int(input("enter n :"))
for i in range(1, n + 1):
    print(i)

#44.print n to 1
n = int(input("enter n :"))
for i in range(n, 0, -1):
    print(i)

#45.even numbers
n = int(input("enter n :"))
for i in range(2, n + 1, 2):
    print(i)

#46.odd numbers
n = int(input("enter n :"))
for i in range(1, n + 1, 2):
    print(i)

#47.sum of natural numbers
n = int(input("enter n :"))
total = 0
for i in range(1, n + 1):
    total = total + i
print("sum :", total)
