import sys
input = sys.stdin.readline

N,H = map(int, input().split())
A= [ int(input()) for _ in range(N)]
prefix=[0 for _ in range(H+1)]
prefix2=[0 for _ in range(H+1)]
down = A[::2]
up = A[1::2]    

down.sort(reverse=True)
up.sort(reverse=True)

idx=down[0] 
for i in range(len(down)):
    if down[i]==idx:
        prefix[idx]+=1
    
    else:
        idx=down[i]
        prefix[idx]+=1

for i in range(H-1,0,-1):
    prefix[i]+=prefix[i+1]

idx=up[0] 
for i in range(len(up)):
    if up[i]==idx:
        prefix2[idx]+=1
        
    else:  
        idx=up[i]
        prefix2[idx]+=1
        
for i in range(H-1, 0,-1):
    prefix2[i]+=prefix2[i+1]
    

for i in range(1, H+1):
    prefix[i] += prefix2[H+1-i]
    
sol=prefix[1:]
tmp = min(sol)

print(tmp,sol.count(tmp))