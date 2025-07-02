n= int(input())

cnt = 0
mem = set()
for _ in range(n):
    i = input()
    if i == 'ENTER':
        mem.clear()
    else :
        if i not in mem:
            cnt+=1
        mem.add(i)
print(cnt)