#65.multiplication table

n = int(input("enter n :"))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#66.even odd sum

n = int(input("enter n :"))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print("even sum :", even_sum)
print("odd sum :", odd_sum)

#67.armstrong number

n = int(input("enter n :"))
temp = n
digits = str(n)
power = len(digits)
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10
if total == n:
    print("armstrong number")
else:
    print("not an armstrong number")

#68.largest smallest digit

n = int(input("enter n :"))
digits = str(abs(n))
largest = int(digits[0])
smallest = int(digits[0])
for i in digits:
    digit = int(i)
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
print("largest digit :", largest)
print("smallest digit :", smallest)

#69.factors

n = int(input("enter n :"))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

  #70.perfect number

n = int(input("enter n :"))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
if total == n:
    print("perfect number")
else:
    print("not a perfect number")

#71.decimal to binary

n = int(input("enter decimal number :"))
if n == 0:
    binary = "0"
else:
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
print("binary :", binary)

#72.binary to decimal

binary = input("enter binary number :")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("decimal :", decimal)

#73.count and average

count = 0
total = 0
while True:
    n = float(input("enter number (-1 to stop) :"))
    if n == -1:
        break
    count = count + 1
    total = total + n
if count > 0:
    print("count :", count)
    print("average :", total / count)
else:
    print("no numbers entered")

#74.sin series

x = float(input("enter x in radians :"))
n = int(input("enter number of terms :"))
result = 0
sign = 1
for i in range(n):
    power = 2 * i + 1
    factorial = 1
    for j in range(1, power + 1):
        factorial = factorial * j
    term = (x ** power) / factorial
    result = result + sign * term
    sign = sign * -1
print("sin value :", result)

#75.string palindrome recursion

def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
s = input("enter string :")
if palindrome(s):
    print("palindrome")
else:
    print("not palindrome")

#76.count vowels recursion

def count_vowels(s):
    if len(s) == 0:
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
s = input("enter string :")
print("number of vowels :", count_vowels(s))

#77.increasing decreasing recursion

def inc_dec(i, n):
    if i > n:
        return
    print(i, end=" ")
    inc_dec(i + 1, n)
    print(i, end=" ")
n = int(input("enter n :"))
inc_dec(1, n)
