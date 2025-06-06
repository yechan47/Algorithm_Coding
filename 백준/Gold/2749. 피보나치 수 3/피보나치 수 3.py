import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
p = 100000
q = 1000000
n = n % (15*p)

for i in range(n):
    a, b = b%q, (a+b)%q
print(a)