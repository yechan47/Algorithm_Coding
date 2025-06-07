n = int(input())
n_list = input()

color = [0,0]
if n_list[0] == 'R':
    color[0]+=1
else:
    color[1]+=1

for i in range(1,n):
    if n_list[i] == 'R':
        if n_list[i-1] != n_list[i]:
            color[0]+=1

    elif n_list[i] == 'B':
        if n_list[i-1] != n_list[i]:
            color[1]+=1

print(min(color[0],color[1])+1)