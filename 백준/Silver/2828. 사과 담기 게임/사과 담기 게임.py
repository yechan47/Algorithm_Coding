import sys
input = sys.stdin.readline

n, m = map(int, input().split())
apple = int(input())

left = 1
right = m
sum = 0

for _ in range(apple):
    where = int(input())
    
    if left <= where and where <= right:
        continue
        
    if left > where:
        sum += (left - where)
        right -= (left - where)
        left = where
    else:
        sum += (where - right)
        left += (where - right)
        right = where

print(sum)