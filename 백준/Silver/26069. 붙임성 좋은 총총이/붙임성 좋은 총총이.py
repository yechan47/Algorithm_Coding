from sys import stdin

input = stdin.readline

n = int(input())
chong = set(['ChongChong'])

for _ in range(n):
    a, b = input().split()
    if a in chong or b in chong:
        chong.update([a, b])

print(len(chong))