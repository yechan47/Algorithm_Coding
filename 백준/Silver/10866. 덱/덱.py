from collections import deque
import sys

n = int(input())
d = deque([])

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push_front':
        d.appendleft(int(a[1]))
        
    elif a[0] == 'push_back':
        d.append(int(a[1]))
        
    elif a[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
            
    elif a[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
            
    elif a[0] == 'size':
        print(len(d))
        
    elif a[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
            
    elif a[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
            
    elif a[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)