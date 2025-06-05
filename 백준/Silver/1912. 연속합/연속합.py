import sys
input= sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))
hap = [0] * n
hap[0] = m[0]

for i in range(1, n):
    hap[i] = max(m[i], hap[i-1] + m[i])

print(max(hap))
