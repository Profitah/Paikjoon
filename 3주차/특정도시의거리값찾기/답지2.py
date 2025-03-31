import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)

result = []
visited = [False] * (N + 1)
distance = [0] * (N + 1)
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
              queue.append(i)
              visited[i] = True
              distance[i] = distance[x] + 1

              if distance[i] == K:
                  result.append(i)
            
bfs(X)
if len(result) == 0: print(-1)
else:
  result.sort()
  for data in result:
      print(data)