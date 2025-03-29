from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
방문 = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(visit):
    방문[visit] = True
    print(visit, end=' ')  
    for i in graph[visit]:
        if not 방문[i]:
            dfs(i)

def bfs(visit):
    q = deque([visit])
    방문[visit] = True
    while q:
        qpop = q.popleft()
        print(qpop, end=' ')  
        for i in graph[qpop]:
            if not 방문[i]:
                방문[i] = True
                q.append(i)

dfs(v)
print() 
방문 = [False] * (n + 1)
bfs(v)