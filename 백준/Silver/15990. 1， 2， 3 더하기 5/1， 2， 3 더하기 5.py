t = int(input())
n = []
p = 1000000009

for i in range(t):
    n.append(int(input()))

dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = dp[i - 1][1] % p + dp[i - 1][2] % p
    dp[i][1] = dp[i - 2][0] % p + dp[i - 2][2] % p
    dp[i][2] = dp[i - 3][0] % p + dp[i - 3][1] % p
    
for i in n:
    print(sum(dp[i]) % p)