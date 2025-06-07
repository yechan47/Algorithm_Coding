import sys
input = sys.stdin.readline

n = int(input())
p = 1000000009
dp_table = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1001)] for _ in range(1001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    for j in range(2, 1001):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % p

for dp_table in dp_table:
    print(dp[dp_table[0]][dp_table[1]])