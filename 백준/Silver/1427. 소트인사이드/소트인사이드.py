import sys
input = sys.stdin.readline

n = input()
x = sorted(list(n), reverse = True)

for i in range(len(n)):
    print(x[i], end='')