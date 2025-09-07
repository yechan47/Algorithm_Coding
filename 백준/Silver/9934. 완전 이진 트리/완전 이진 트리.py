import sys
input = sys.stdin.readline

k = int(input())
squence = list(map(int, input().split()))
trees = [[] for _ in range(k)]

def binary_tree(array, depth):
    mid_index = len(array) // 2
    trees[depth].append(array[mid_index])
    if len(array) == 1:
        return
    binary_tree(array[:mid_index], depth + 1)
    binary_tree(array[mid_index+1:], depth + 1)

binary_tree(squence, 0)
for tree in trees:
    print(*tree)