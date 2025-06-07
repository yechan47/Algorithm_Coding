import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0]

for i in range(0, n):
    for j in range(n):
        if a[i] > a[j]:
            dp[i] = max(dp[i], a[i] + dp[j])
        else:
            dp[i] = max(dp[i], a[i])
            
print(max(dp))