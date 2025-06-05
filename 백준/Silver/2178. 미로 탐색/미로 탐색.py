def finding(a,b):
    visited = [[0]* M for _ in range(N)]
    queue = [[a,b]]
    visited[a][b] = 1
    while queue:
        y, x = queue.pop(0)
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and maze[ny][nx] != 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny,nx])
    return visited[N-1][M-1]

import sys
N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
print(finding(0,0))