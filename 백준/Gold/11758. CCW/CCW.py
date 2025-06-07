import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])

a = []

for i in range(3):
    a.append(list(map(int, input().split())))
    
res = ccw(a[0], a[1], a[2])

if res > 0:
    print(1)    
elif res == 0:
    print(0)    
else:
    print(-1)