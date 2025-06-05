P, K = map(int, input().split())
a = K

for i in range(2, K):
    if P % i == 0:
        if a > i:
            a = i

if a != K:
    print('BAD', a)
else:
    print('GOOD')