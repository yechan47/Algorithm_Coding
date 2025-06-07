import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
p = 1000000009

dp = [0 for i in range(100001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3

for i in range(6, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % p

for num in num:
    print(dp[num])