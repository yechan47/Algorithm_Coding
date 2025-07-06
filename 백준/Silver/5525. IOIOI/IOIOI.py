import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

start,end,cnt = 0,0,0

while end < m:
    if s[end:end+3] == "IOI":
        end += 2
        if end - start == 2*n:
            cnt +=1
            start +=2
    else:
        start = end+1
        end = end +1
print(cnt)