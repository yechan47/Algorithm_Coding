import sys
import copy
input = sys.stdin.readline

n = int(input())

now_bulbs = list(map(int,input().strip()))
goal_bulbs = list(map(int,input().strip()))

def press_switch(idx,bulbs):
    if idx-1 >=0:
        convert01(idx-1,bulbs)
    convert01(idx,bulbs)
    if idx+1 < n:
        convert01(idx+1,bulbs)

def convert01(idx,bulbs):
    if bulbs[idx] == 1:
        bulbs[idx] = 0
    else:
        bulbs[idx] = 1

def solution():
    answer = []
    n_bulbs = now_bulbs.copy()
    press_switch(0,n_bulbs)
    cnt = 1
    for i in range(1,n):
        if i-1>=0 and n_bulbs[i-1] != goal_bulbs[i-1]:
            press_switch(i,n_bulbs)
            cnt += 1

    if n_bulbs == goal_bulbs:
        answer.append(cnt)

    cnt = 0
    for i in range(1,n):
        if i-1>=0 and now_bulbs[i-1] != goal_bulbs[i-1]:
            press_switch(i,now_bulbs)
            cnt += 1
            
    if now_bulbs == goal_bulbs:
        answer.append(cnt)

    if answer:
        print(min(answer))
    else:
        print(-1)
solution()