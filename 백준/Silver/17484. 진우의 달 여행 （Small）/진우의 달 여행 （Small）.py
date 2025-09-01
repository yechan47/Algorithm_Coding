def backtracking(cost, row, col, before):
    global res
    if row == N:
        res = cost
        return
    cost += matrix[row][col]
    if res and res < cost:
        return
    for i in range(col-1, col+2):
        if i - col == before:
            continue
        if 0 <= i < M:
            backtracking(cost, row+1, i, i - col)

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(M):
        backtracking(0, 0, i, 2)
    print(res)