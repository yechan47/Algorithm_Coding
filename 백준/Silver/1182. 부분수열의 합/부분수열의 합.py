import sys

def find(pointer, total):
    global answer
    if pointer >= n:
        return
    find(pointer + 1, total)
    total += a[pointer]
    find(pointer + 1, total)
    if total == s:
        answer += 1

n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer = 0

find(0, 0)
print(answer)