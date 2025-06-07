import sys 
input = sys.stdin.readline

n = int(input())
lose = list(map(int, input().split()))
lose.sort()

result = lose[-1]
if n%2==1:
    for i in range(n//2):
        tmp = lose[i]+lose[n-i-2]
        if result < tmp:
            result = tmp
elif n%2==0:
    for i in range(n//2):
        tmp = lose[i]+lose[n-i-1]
        if result < tmp:
            result = tmp
        
print(result)