from collections import deque

N = int(input())
arr = [list(map(int,input())) for i in range(N)]
visited = [[False]*N for i in range(N)] 
dx = [-1, 0, 0, 1]   
dy = [0, 1, -1, 0]
R = []  

def BFS(x,y):
    queue = deque()
    queue.append((x,y)) 
    num = 0      
    if arr[x][y] == 1 and visited[x][y] == False:
        num += 1
        visited[x][y] = True
        
    while queue:
        v,b = queue.popleft()
        
        for i in range(4):
            nx = v + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    num += 1
    return R.append(num)

for i in range(N):
    for j in range(N): 
        if arr[i][j] == 1 and visited[i][j] == False:
            BFS(i,j)
            
print(len(R))
for i in sorted(R):
    print(i)