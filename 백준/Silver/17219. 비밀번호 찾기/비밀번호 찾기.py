import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for _ in range(N):
    a, b = input().split()
    add[a] = b

for _ in range(M):
    print(add[input().rstrip()])