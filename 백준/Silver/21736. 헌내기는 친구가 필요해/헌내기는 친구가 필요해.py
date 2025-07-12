import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

graph = []
for i in range(h):
    graph.append(list(input().strip()))

visited = [[False] * w for _ in range(h)]

x = y = res = 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'I':
            x = j
            y = i
            break

def dfs(y, x):
    global res
    if graph[y][x] == 'P':
        res += 1
    visited[y][x] = True

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if (0<=ny<h) and (0<=nx<w):
            if not visited[ny][nx] and graph[ny][nx] != 'X':
                dfs(ny, nx)

dfs(y, x)

if res == 0:
    print("TT")
else:
    print(res)