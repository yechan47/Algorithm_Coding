import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())


def new_point(point, n):
    return point - 2 ** (n - 1)


def dnc(n, r, c):
    if n == 1:
        return 2 * r + c

    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return dnc(n - 1, r, c)
    elif r < 2 ** (n - 1) and c >= 2 ** (n - 1):
        return 2 ** (2 * n - 2) + dnc(n - 1, r, new_point(c, n))
    elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):
        return 2 ** (2 * n - 1) + dnc(n - 1, new_point(r, n), c)
    else:
        return 3 * 2 ** (2 * n - 2) + dnc(n - 1, new_point(r, n), new_point(c, n))


print(dnc(n, r, c))