n=int(input())
arr=list(map(int,input().split()))
num=[0]*n
arr.reverse()
m=n
for i in range(n):
    a=arr[i]
    for j in range(n-1,a,-1):
        num[j]=num[j-1]
    num[a]=m;
    m-=1
for i in range(n):
    print(num[i],end=" ")