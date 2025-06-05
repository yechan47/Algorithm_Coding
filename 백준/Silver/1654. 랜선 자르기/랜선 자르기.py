K, N = map(int, input().split())
lines = list()

for i in range(K):
    lines.append(int(input()))

lines.sort()
mMin = 1
mMax = lines[len(lines) - 1]
cnt = 0

while mMin <= mMax:
    cnt = 0 
    mid = (mMin + mMax) // 2  
    for line in lines:
        cnt += line // mid

    if cnt >= N: 
        mMin = mid + 1
    else:
        mMax = mid - 1

print(mMin - 1)