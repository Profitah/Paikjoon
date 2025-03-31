 # 인접 리스트와 BFS를 이용한 최단 거리 K 도시 찾기
import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력을 위한 설정

# 입력 처리
n, m, k, x = map(int, input().split())  # 도시 수n, 도로 수m, 목표 거리 k, 출발 도시 x

# 거리 정보를 저장할 리스트 (-1: 방문하지 않음)
road_distance = [-1] * (n + 1)

# 인접 리스트 생성 (1번 도시부터 n번 도시까지 사용)
graph = []
for i in range(n + 1):
    graph.append([])  # 각 도시마다 연결된 도시를 저장할 리스트 추가

# 간선 정보 입력 → 인접 리스트에 저장
for j in range(m):
    a, b = map(int, input().split())  # a번 도시에서 b번 도시로 이동 가능 (단방향)
    graph[a].append(b)

# BFS 함수 정의
def bfs(start):
    q = deque([start])  # 시작 도시를 큐에 삽입
    road_distance[start] = 0  # 시작 도시의 거리는 0

    while q:
        current = q.popleft()  # 큐에서 현재 도시 꺼내기
        for next_city in graph[current]:  # 연결된 도시들 탐색
            if road_distance[next_city] == -1:  # 방문하지 않은 도시라면
                # 현재 도시 거리 + 1을 저장 (최단 거리 보장)
                road_distance[next_city] = road_distance[current] + 1
                q.append(next_city)  # 다음 도시를 큐에 삽입

# BFS 실행
bfs(x)

# 거리 K인 도시를 찾고 출력
found = False  # 조건에 맞는 도시가 있는지 여부
for i in range(1, n + 1):
    if road_distance[i] == k:
        print(i)
        found = True

# 조건에 맞는 도시가 하나도 없다면 -1 출력
if not found:
    print(-1)