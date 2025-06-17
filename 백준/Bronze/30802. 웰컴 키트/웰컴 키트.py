n = int(input())
Shirts = list(map(int,input().split()))
T,P = map(int,input().split())
total = 0

for i in Shirts:
    total += i // T
    if i % T:
        total += 1
print(total)
print(n // P, n % P)