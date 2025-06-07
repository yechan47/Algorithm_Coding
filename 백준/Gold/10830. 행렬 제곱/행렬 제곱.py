import sys

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def multiplication(n, a, b):
    result = [[0] * n for _ in range(n)]
    for row in range(n):
        for column in range(n):
            for i in range(n):
                result[row][column] += a[row][i] * b[i][column]
            result[row][column] %= 1000
    return result


def cal(n, b, a):
    if b == 1:
        return a
    elif b == 2:
        return multiplication(n, a, a)
    else:
        temp = cal(n, b // 2, a)
        if b % 2 == 0:
            return multiplication(n, temp, temp)
        else:
            return multiplication(n, multiplication(n, temp, temp), a)


result = cal(N, B, A)

for c in result:
    for num in c:
        print(num % 1000, end=' ')
    print()