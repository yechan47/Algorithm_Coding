import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    cnt=0
    i=5
    while i<=x:
        cnt+=x//i
        i*=5
    print(cnt)