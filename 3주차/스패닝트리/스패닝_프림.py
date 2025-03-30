# 사실... 과거에 풀었던 이력이 있어서 그대로 가져왔습니다.
import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
edges = [[] for i in range(V+1)]
visited = [False] * (V+1)
heap = [(0, 1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s].append((w, e))
    edges[e].append((w, s))
    
ans = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    ans += w
    cnt += 1
    for edge in edges[node]:
        heapq.heappush(heap, edge)
        
print(ans)