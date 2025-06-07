n = int(input())
li = []

for _ in range(n):
	a = int(input())
	li.append(a)
    
li.sort(reverse=True)
ans = 0

for i in range(n):
	if (i+1) % 3 != 0:
		ans += li[i]

print(ans)
