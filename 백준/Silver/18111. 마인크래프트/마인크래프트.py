I=lambda:map(int,input().split())
n,m,b=I()
l=[]

for i in range(n):l.extend(I())
dic={}
for i in l:
    if i not in dic:
        dic[i]=1 
    else:
        dic[i]+=1
rt=8**9
rh=0

for i in range(min(l),max(l)+1): 
    t=0 
    tb=b 
    for j in dic:
        q=dic.get(j)
        if j>i:
            t+=(j-i)*q*2
            tb+=(j-i)*q
        else:
            t+=(i-j)*q 
            tb-=(i-j)*q 
    if tb>=0:
        if t<=rt:
            rt=t
            rh=i
print(rt,rh)