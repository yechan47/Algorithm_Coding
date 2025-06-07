n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []

c = a+b
c.sort()

print(" ".join(map(str,c)))
