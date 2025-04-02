import heapq
import sys

def bfs():
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

# 리스트 컴프리헨션 대신 반복문으로 초기화
answer = [0] * (N + 1)  # 먼저 0으로 초기화
for i in range(N + 1):
    answer[i] = int(1e9)  # 각 요소를 무한대 값으로 설정

bfs()

print(answer[end])