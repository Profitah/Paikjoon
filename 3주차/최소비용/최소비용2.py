import heapq
import sys

def BFS():
    queue = []
    heapq.heappush(queue, (0, start))
    answer[start] = 0

    while queue:
        c, node = heapq.heappop(queue)
        if answer[node] < c:
            continue
        for next, cost in graph[node]:
            if answer[next] > answer[node] + cost:
                answer[next] = answer[node] + cost
                heapq.heappush(queue, (answer[next], next))

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[] for i in range(N + 1)]

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))

start, end = map(int, sys.stdin.readline().split())

answer = [int(1e9) for _ in range(N + 1)]

BFS()

print(answer[end])