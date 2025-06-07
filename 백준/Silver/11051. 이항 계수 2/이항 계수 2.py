import sys
input = sys.stdin.readline

def factorial(i):
    a = 1
    for x in range(2, i+1):
        a *= x
    return a

n, k = map(int, input().split())

result = factorial(n) // (factorial(n-k) * factorial(k))
print(result % 10007)