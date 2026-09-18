#55.factorial

n = int(input("enter n :"))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("factorial :", factorial)

#56.prime check

n = int(input("enter n :"))
prime = True
if n <= 1:
    prime = False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
if prime:
    print("prime number")
else:
    print("not a prime number")

#57.print prime numbers

n = int(input("enter n :"))
for num in range(2, n + 1):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

  #58.gcd hcf

a = int(input("enter a :"))
b = int(input("enter b :"))
x = a
y = b
while y != 0:
    x, y = y, x % y
print("gcd :", x)

#59.lcm

a = int(input("enter a :"))
b = int(input("enter b :"))
x = a
y = b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print("lcm :", lcm)
