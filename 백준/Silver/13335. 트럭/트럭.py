import sys
input=sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w
time = 0
while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)