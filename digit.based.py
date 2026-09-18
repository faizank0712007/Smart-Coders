#48.count digits
n = int(input("enter n :"))
n = abs(n)
count = 0
if n == 0:
    count = 1
while n > 0:
    count = count + 1
    n = n // 10
print("number of digits :", count)

#49.sum of digits

n = int(input("enter n :"))
n = abs(n)
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print("sum of digits :", total)

#50.reverse number

n = int(input("enter n :"))
temp = abs(n)
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if n < 0:
    reverse = -reverse
print("reverse :", reverse)

#51.palindrome number

n = int(input("enter n :"))
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if n == reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")

#52.happy number

n = int(input("enter n :"))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit * digit
        n = n // 10
    n = total
if n == 1:
    print("happy number")
else:
    print("not a happy number")

#53.product of digits using recursion

def product(n):
    if n < 10:
        return n
    return (n % 10) * product(n // 10)
n = int(input("enter n :"))
print("product of digits :", product(abs(n)))

#54.extract digits

n = int(input("enter n :"))
digits = str(abs(n))
for i in digits:
    print(i)
