import sys

n = int(sys.stdin.readline())
s = []

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
      s.append(a[1])
    
    elif a[0] == "pop":
      if len(s):
        print(s.pop())
      else:
        print(-1)

    elif a[0] == "size":
      print(len(s))

    elif a[0] == "empty":
      if len(s):
        print(0)
      else:
        print(1)

    elif a[0] == "top":
      if len(s):
        print(s[-1])
      else:
        print(-1)