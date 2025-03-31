import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split()) # 

road_distance = [-1] * (n + 1)

graph = []
for i in range(n + 1):
    graph.append([])

for j in range(m):
    a, b = map(int, input().split())  
    graph[a].append(b)  

def bfs(start):
    q = deque([start])
    road_distance[start] = 0  

    while q:
        current = q.popleft()

        for next_city in graph[current]:
            if road_distance[next_city] == -1:
                road_distance[next_city] = road_distance[current] + 1
                q.append(next_city)

bfs(x)

found = False
for i in range(1, n + 1):
    if road_distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
