n = int(input())
p = list(map(int, input().split()))

p.sort()
a = 0

for x in range(1, n+1):
    a += sum(p[0:x])
    
print(a)