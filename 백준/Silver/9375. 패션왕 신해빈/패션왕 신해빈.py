import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    dic = dict()
    for i in range(n):
        x, y = input().split()
        if y in dic:
            dic[y].append(x)
        else:
            dic[y] = [x]
    
    arr = list(dic.values())
    ans = 1
    for i in arr:
        ans *= len(i)+1
    print(ans-1)