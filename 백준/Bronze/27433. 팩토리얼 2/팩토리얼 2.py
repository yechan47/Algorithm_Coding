import sys
def factorial(n):
    result = 1
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
input=sys.stdin.readline
N = int(input())
print(factorial(N))