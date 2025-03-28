# dfs를 이용한 그래프 탐색 프로그램

n = int(input())  # 컴퓨터(정점)의 수 입력
v = int(input())  # 연결된 쌍(간선)의 수 입력
graph = []  # 빈 리스트 생성

for i in range(n + 1):  # 0번부터 n번까지 반복
    graph.append([])  # 빈 리스트를 추가하여 초기화

visited = [0] * (n + 1)  # 방문 여부를 체크하는 리스트 (초기값은 0) 

for i in range(v):  # 간선 수만큼 반복하여
    a, b = map(int, input().split())  # 연결된 두 정점 입력
    graph[a] += [b]  # a에 b를 연결 (무방향 그래프) # a + a+b
    graph[b] += [a]  # b에 a도 연결 # b + b+a

def dfs(v):  # 깊이 우선 탐색 재귀 함수
    visited[v] = 1  # 현재 노드를 방문 표시
    for nx in graph[v]:  # 연결된 모든 노드에 대해
        if visited[nx] == 0:  # 아직 방문하지 않았다면
            dfs(nx)  # 그 노드로 이동하여 재귀 탐색

dfs(1)  # 1번 컴퓨터(정점)부터 바이러스 전파 시작
print(sum(visited) - 1)  # 1번을 제외한 감염된 컴퓨터 수 출력