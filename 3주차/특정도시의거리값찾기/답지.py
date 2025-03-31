import sys                          # 빠른 입력을 위해 sys 모듈 사용
from collections import deque       # BFS를 위한 큐 자료구조 deque 사용

input = sys.stdin.readline          # 입력 속도를 높이기 위한 빠른 입력 함수 지정

n, m, k, x = map(int, input().split())  
# n: 도시의 개수
# m: 도로의 개수
# k: 목표 거리
# x: 출발 도시

# 인접 리스트 초기화 
graph = []
for i in range(n + 1):
    graph.append([])

# 거리 정보 초기화 (-1로 시작)
distance = []
for i in range(n + 1):
    distance.append(-1)

# 간선 정보 입력받아 인접 리스트에 저장
for i in range(m):
    a, b = map(int, input().split())  
    graph[a].append(b)              # a에서 b로 가는 단방향 도로 저장

# BFS 함수 정의: 시작 도시부터 탐색 시작
def bfs(start):
    q = deque()                     # 큐 생성
    q.append(start)                 # 시작 도시를 큐에 삽입
    distance[start] = 0             # 시작 도시는 거리 0으로 설정

    while q:                        # 큐가 빌 때까지 반복
        now = q.popleft()          # 현재 도시 꺼내기

        for next_city in graph[now]:         # 현재 도시와 연결된 도시들 순회
            if distance[next_city] == -1:    # 아직 방문하지 않은 도시라면
                distance[next_city] = distance[now] + 1  # 현재 도시 거리 + 1로 설정
                q.append(next_city)                     # 해당 도시를 큐에 삽입

bfs(x)  # 출발 도시 x부터 BFS 시작

found = False                      # 출력할 도시가 있는지 확인하기 위한 플래그

for i in range(1, n + 1):          # 모든 도시를 순회하면서
    if distance[i] == k:           # 거리 k인 도시를 찾으면
        print(i)                   # 도시 번호 출력
        found = True               # 하나라도 찾았다는 표시

if not found:                      # 거리 k인 도시를 하나도 못 찾았다면
    print(-1)                      # -1 출력