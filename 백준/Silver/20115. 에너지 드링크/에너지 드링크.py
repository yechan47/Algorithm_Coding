n = int(input())
ed = list(map(int, input().split()))

ed.sort(reverse = True)
sum = ed[0]

for i in range(1, n):
    sum += ed[i]/2
    
print(sum)
