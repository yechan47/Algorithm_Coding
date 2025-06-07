import sys
input = sys.stdin.readline
p = 1000000007

def factorial(i):
    result = 1
    for x in range(2, i+1):
        result = (result * x) % p
    return result

def power(x, y):
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2
        x = (x * x) % p
    return result

n, k = map(int, input().split())

result = (factorial(n) * power(factorial(k) * factorial(n - k), p - 2)) % p
print(result)