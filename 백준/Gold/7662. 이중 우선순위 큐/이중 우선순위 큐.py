import sys
import heapq


def sync(arr):
    while arr and deleted[arr[0][1]]:
        heapq.heappop(arr)


input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    max_heap = []
    min_heap = []
    k = int(input())
    deleted = [True] * k

    for i in range(k):
        s, num = input().split()

        if s == "I":
            heapq.heappush(max_heap, (-1 * int(num), i))
            heapq.heappush(min_heap, (int(num), i))
            deleted[i] = False

        else:
            if num == "1":
                sync(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)

            elif num == "-1":
                sync(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)

    sync(max_heap)
    sync(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")