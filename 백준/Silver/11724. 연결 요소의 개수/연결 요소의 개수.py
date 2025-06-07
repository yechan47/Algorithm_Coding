def sum(i):
    for j in range(len(l)):
        if i!=j:
            if a in l[j] or b in l[j]:
                l[i]=l[i] | l[j]
                l.pop(j)
                return sum(i)

import sys
N,M=map(int,sys.stdin.readline().split())
l=[]
n=list(range(1,N+1))
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if a in n:
        n.remove(a)
    if b in n:
        n.remove(b)
    if l:
        for i in range(len(l)):
            if a in l[i] or b in l[i]:
                if a in l[i]:
                    l[i].add(b)
                elif b in l[i]:
                    l[i].add(a)
                sum(i)
                break
            if i==len(l)-1:
                l.append(set([a,b]))
    else:
        l.append(set([a,b]))
print(len(l)+len(n))