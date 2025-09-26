def dfs(graph, v, already, depth):
    global ans

    r, c = v
    stack = set()
    stack.add((r, c, already+graph[r][c], depth))

    while stack:
        nowr, nowc, nowalready, nowdepth = stack.pop()
        ans = max(ans, nowdepth)
        for i in range(4):
            newr, newc = nowr+dr[i], nowc+dc[i]
            if 0 <= newr < R and 0 <= newc < C and graph[newr][newc] not in nowalready:
                stack.add((newr, newc, nowalready + graph[newr][newc], nowdepth+1))
    return

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

ans = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dfs(graph, (0, 0), '', 1)

print(ans)