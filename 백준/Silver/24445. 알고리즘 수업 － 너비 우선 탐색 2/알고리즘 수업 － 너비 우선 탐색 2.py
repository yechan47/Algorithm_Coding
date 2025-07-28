from collections import deque, defaultdict
import sys
input = sys.stdin.readline

graph = defaultdict(list)
N, M, R = map(int,input().split())
for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(R) :
    queue = deque()
    queue.append(R)
    visited = [0 for _ in range(N+1)]
    visited[R] = 1
    cnt = 1

    while(queue) :
        curNode = queue.popleft()
        visited[curNode] = cnt
        cnt += 1

        nextNode = graph[curNode]
        nextNode.sort(reverse=True)
        for nn in nextNode:
            if( visited[nn] == 0):
                visited[nn] = 1
                queue.append(nn)
    return visited

result = BFS(R)

for v in range(1,N+1):
    print(result[v])