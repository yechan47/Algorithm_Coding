n = int(input())

L = [0]*(n+1)

for i in range(2,n+1):
    L[i] = L[i-1]+1
    if i%2 == 0:
        L[i] = min(L[i],L[i//2]+1)
    if i%3 == 0:
        L[i] = min(L[i],L[i//3]+1)
        
print(L[n])