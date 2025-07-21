n, m = map(int, input().split())
num = list(map(int, input().split()))

set_num = list(set(num))
set_num.sort()


dict = []

def backtracking(idx):
    global dict
    
    if len(dict) == m : 
        print(*dict)
        return
        
    for i in range(idx, len(set_num)):
        dict.append(set_num[i])
        backtracking(i) 
        dict.pop()
        
backtracking(0)