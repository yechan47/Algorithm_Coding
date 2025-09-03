def count_candy():
  max_count = 0
  for i in range(n):
    count = 1
    for j in range(n - 1):
      if board[i][j] == board[i][j + 1]:
        count += 1
      else: 
        count = 1
      max_count = max(max_count, count)

  for j in range(n):
    count = 1 
    for i in range(n - 1):
      if board[i][j] == board[i + 1][j]:
        count += 1
      else: 
        count = 1 
      max_count = max(max_count, count)
  return max_count

n = int(input())

board = []
for _ in range(n):
  board.append(list(input()))

max_value = 0 
for i in range(n):
  for j in range(n):
    if j < n - 1 and board[i][j] != board[i][j + 1]:
      board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
      max_value = max(max_value, count_candy())
      board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    if i < n - 1 and board[i][j] != board[i + 1][j]:
      board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
      max_value = max(max_value, count_candy()) 
      board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(max_value)