n = int(input())
w = []
ans = 0

for i in range(n):
    r = int(input())
    w.append(r)
    
w.sort()

for j in range(len(w)):
    if w[j] * n > ans:
        ans = w[j] * n
    n -= 1
    
print(ans)