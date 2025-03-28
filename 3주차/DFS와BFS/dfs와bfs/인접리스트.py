from collections import deque

n,m,v = int(input())

# 인접 리스트 만들기
graph = []
for i in range(n + 1):
    graph.append([])

# 방문 여부를 체크할 리스트 만들기
visited = []
for i in range(n + 1):
    visited.append(False)

# 간선 입력받기
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 오름차순 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 함수 (재귀)
def dfs(visit):
    visited[visit] = True
    print(visit, end=' ')
    for i in graph[visit]:
        if not visited[i]:
            dfs(i)

# BFS 함수 (queue)
def bfs(visit):
    queue = deque([visit])
    visited[visit] = True
    while queue:
        visit = queue.popleft()
        print(visit, end=' ')
        for i in graph[visit]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
# DFS 호출
dfs(v)
print()

# BFS 호출
visited = [False] * (n+1)
bfs(v)
print()






