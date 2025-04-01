# 강의에서 나온 코드이기 때문에... 당연히 정답이다. 온전히 내 것으로 만드는데 시간이 필요하다.

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def topologySort(n, graph):
    in_degree = [0] * (n + 1)

    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    result = []

    while q:
        x = q.popleft()
        result.append(x)

        for y in graph[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)

    return result

print(*topologySort(n, graph))