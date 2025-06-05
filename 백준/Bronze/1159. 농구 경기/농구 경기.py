import sys
input= sys.stdin.readline

n = int(input())
name = []
res = []

for i in range(n):
    a = input()
    name.append(a[0])

fname = set(name)

for i in fname:
    if name.count(i) >= 5:
        res.append(i)

if len(res) > 0:
    print(''.join(sorted(res)))
else:
    print("PREDAJA")
