import sys
input = sys.stdin.readline

p = 1000000007
m = int(input())

def div(a, x):
    if x == 1:
        return a
    if x % 2 == 0:
        return div(a, x//2)**2 % p
    else:
        return div(a, x-1)*a % p
        
factorial = [1]*4000001
for i in range(2, 4000001):
    factorial[i] = factorial[i-1]*i % p
    
for _ in range(m):
    n, k = map(int, input().split())
    print(factorial[n]*div(factorial[n-k]*factorial[k]%p, p-2) % p)
