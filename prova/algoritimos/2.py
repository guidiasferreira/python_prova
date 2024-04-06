
n = 0
m = 1000

while n <= m:
    n = n + 1

    if n % 10 == 0 or n % 10 == 6:
        continue

    if n % 17 == 0:
        print(n)

