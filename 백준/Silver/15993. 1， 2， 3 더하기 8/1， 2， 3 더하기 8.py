import sys
input = sys.stdin.readline

n = int(input())
p = 1000000009
dp_table = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(2)] for _ in range(100001)]
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 2
dp[3][1] = 2

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % p
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % p

for dp_table in dp_table:
    print(str(dp[dp_table][1]) + " " + str(dp[dp_table][0]))