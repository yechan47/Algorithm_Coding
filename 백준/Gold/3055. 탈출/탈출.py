from collections import deque
import sys

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def waterBFS():
    waterSize = len(waterQ)
    while waterSize:
        nowx, nowy = waterQ.popleft()
        for x, y in zip(dx,dy):
            nx = x+nowx
            ny = y+nowy
            if nx == end[0] and ny == end[1]:
                continue
            if nx < 0 or nx >= w or ny < 0 or ny >= h or board[ny][nx] == -1:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = board[nowy][nowx] + 1
                waterQ.append((nx,ny))
        waterSize -= 1

def personBFS(start):
    q = deque()
    q.append(start)
    visit[start[1]][start[0]] = 1
    while q:
        qSize = len(q)
        while qSize:
            nowx, nowy = q.popleft()
            if nowx == end[0] and nowy == end[1]:
                return visit[nowy][nowx] - 1
            for x, y in zip(dx,dy):
                nx = x + nowx
                ny = y + nowy
                if nx < 0 or nx >= w or ny < 0 or ny >= h or board[ny][nx] == -1:
                    continue
                if board[ny][nx] == 0 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[nowy][nowx] + 1
                    q.append((nx,ny))
            qSize -= 1
        waterBFS()
    return 'KAKTUS'

h, w = map(int,input().split(' '))
board = [[0] * (w) for _ in range(h)]
visit = [[0] * (w) for _ in range(h)]

waterQ = deque()
for i in range(h):
    item = input()
    for j in range(w):
        if item[j] == 'X':
            board[i][j] = -1
        elif item[j] == '*':
            board[i][j] = 1
            waterQ.append((j,i))
        elif item[j] == '.':
            board[i][j] = 0
        elif item[j] == 'S':
            board[i][j] = 0
            start = (j,i)
        else:
            board[i][j] = 0
            end = (j,i)
waterBFS()
ans = personBFS(start)
print(ans)     