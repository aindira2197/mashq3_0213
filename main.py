# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        s += i
print(s)

# 2
n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 5 == 0:
        count += 1
print(count)

# 3
n = int(input())
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

# 4
n = int(input())
summa = 0
while n > 0:
    summa += n % 10
    n //= 10
print(summa)

# 5
n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
