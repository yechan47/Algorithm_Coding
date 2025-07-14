import sys
from itertools import combinations
def solution():
    n = int(sys.stdin.readline().strip())
    graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
    min_diff = float('inf')
    player = list(range(n))
    team = list(combinations(player, n //2))
    for idx in range(len(team) // 2): 
        start_team = set(team[idx])
        link_team = set(player) - start_team
        
        start_score = sum(graph[i][j] for i, j in combinations(start_team, 2)) + \
            sum(graph[j][i] for i, j in combinations(start_team, 2))
        link_score = sum(graph[i][j] for i, j in combinations(link_team, 2)) + \
            sum(graph[j][i] for i, j in combinations(link_team, 2))
            
        min_diff = min(min_diff, abs(start_score - link_score))
    return min_diff
print(solution())