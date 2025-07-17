import sys


n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda x: x[0])
dp = [0] * n

for i in range(n):
    result_max = 0
    for j in range(i):
        if m[i][1] > m[j][1]:
            if result_max < dp[j]:
                result_max = dp[j]

    dp[i] = result_max + 1

print(n - max(dp))