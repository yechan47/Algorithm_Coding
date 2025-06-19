l = list(input().split(' '))
n = str(l[0])
b = int(l[1])

alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = 0

if n == '0':
  print(0)

else:
  m = len(n)-1

  for i in range(m, -1, -1):
    res += alpha.index(n[m-i])*(b**i)

print(res)