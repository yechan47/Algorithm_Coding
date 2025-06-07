import sys
input = sys.stdin.readline

n = int(input())
p = 1000000009
dp_table = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 2
dp[3][1] = 1
dp[3][2] = 3
dp[3][3] = 4

for i in range(4, 1001):
    for j in range(2, 1001):
        if i < j:
            break

        dp[i][j] = dp[i][j-1]
        for k in range(1, 4):
            if dp[i - k][j - 1] > 0:
                dp[i][j] = (dp[i][j] + (dp[i-k][j-1] - dp[i-k][j-2])) % p


for dp_table in dp_table:
    print(dp[dp_table[0]][dp_table[1]])