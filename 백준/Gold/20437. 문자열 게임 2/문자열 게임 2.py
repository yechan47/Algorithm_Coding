from collections import defaultdict

num = int(input())

for _ in range(num):
    w = input().strip()
    k = int(input())

    alpha = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            alpha[w[i]].append(i)
            
    if alpha:
        result = []
        for alpha_list in alpha.values():
            for i in range(len(alpha_list)-k+1):
                result.append(alpha_list[i+k-1] - alpha_list[i] + 1)
        print(min(result), max(result))
    else:
        print(-1)