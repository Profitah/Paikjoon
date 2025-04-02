import sys
from collections import deque

input = sys.stdin.readline  

K = int(input())  

def is_bipartite(V, E, edges):
    graph = [[] for _ in range(V + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [-1] * (V + 1)
    
    for start in range(1, V + 1):
        if colors[start] != -1:
            continue
            
        queue = deque([start])
        colors[start] = 0
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:
                    return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for i in range(E)]  

    print("YES" if is_bipartite(V, E, edges) else "NO")