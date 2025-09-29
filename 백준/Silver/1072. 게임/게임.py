import math
def get_winning_rate(x, y):
    return (y * 100) // x

x, y = map(int, input().split())
z = get_winning_rate(x, y)
start, end = 1, x
result = 0

if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        temp_z = get_winning_rate(x + mid, y + mid)

        if temp_z > z:
            end = mid - 1
            result = mid
        else:
           start = mid + 1
    print(result)