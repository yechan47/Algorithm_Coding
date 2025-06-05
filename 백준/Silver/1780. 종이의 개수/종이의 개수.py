# acmicpc.net : 2630

def cntJob(n, sx, sy):
     global white, blue, red

     # 크기가 1인 경우
     if n == 1:
          if M[sx][sy] == -1: white += 1
          elif M[sx][sy] == 0: blue += 1
          else: red += 1
          return

     # 모두 같은 값으로 채워져 있는지 검사
     isSame = True
     value = M[sx][sy]

     for i in range(sx, sx+n):
          for j in range(sy, sy+n):
               if M[i][j] != value:
                    isSame = False
                    break

     if isSame:
          if value == -1: white += 1
          elif value == 0: blue += 1
          else: red += 1
          return

     # 분할
     m = n//3
     for i in range(3):
          for j in range(3):
               cntJob(m, sx+i*m, sy+j*m)

# main program
n = int(input())
M = []
for i in range(n):
     M.append([int(x) for x in input().split()])

# white, blue : 빨간색, 파란색 색종이의 개수
white = blue = red = 0
cntJob(n, 0, 0)
print(white)
print(blue)
print(red)
