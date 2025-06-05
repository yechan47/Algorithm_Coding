import sys
input = sys.stdin.readline

p = 1000000000
memory = {1:1,2:1,3:2,4:3,5:5}

def Fibo(n):
  if memory.get(n):
    return memory[n]
  else:
    if n%2 == 1:
      memory[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2) % p
    else:
      memory[n] = (Fibo(n+1)-Fibo(n-1)) % p
    return memory[n]

a,b = map(int,input().split())
print((Fibo(b+2)-Fibo(a+1)) % p)