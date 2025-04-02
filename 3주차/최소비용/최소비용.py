# 실패 

import heapq

INF = int(1e9)

N = int(input())  # 노드 수
M = int(input())  # 간선 수

graph = 1

# 간선 입력
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start = int(input())  # 시작 노드

def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] < cost:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if dist[neighbor] > new_cost:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return dist

dist = dijkstra(start)
for i in range(1, N + 1):
    print(dist[i] if dist[i] != INF else "INF")