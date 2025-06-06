def ncr(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

a, b = map(int, input().split())
print(ncr(a) // (ncr(a-b) * ncr(b)))