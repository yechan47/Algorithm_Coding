def dfs(depth):
    if depth == m:
        print(*ans)
        return
    
    for i in range(n):
        ans.append(num[i])
        dfs(depth + 1)
        ans.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []

dfs(0)