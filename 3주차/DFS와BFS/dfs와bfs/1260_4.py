from collections import deque

n, m, start = map(int, input().split())  
graph = [[] for i in range(n + 1)]     
visited_dfs = [False] * (n + 1)         
visited_bfs = [False] * (n + 1)          

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  

for g in graph:
    g.sort()

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in graph[current]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

dfs(start)
print()
bfs(start)