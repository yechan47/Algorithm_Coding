import sys
n = int(input())
S = []
result = []
a = 1

for i in range(n):
    k=int(sys.stdin.readline().rstrip())
    while a<=k:
        S.append(a)
        result.append('+')
        a+=1
        
    if(S and S[-1]==k):
       S.pop()
       result.append('-')

    else:
        result = ["NO"]
        break

print('\n'.join(result))