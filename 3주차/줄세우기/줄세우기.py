import heapq
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 학생 수 n, 정보 수 m 입력 받음
n, m =  map(int, input().split())

# 학생 번호가 1번부터 시작하므로 n+1 크기로 그래프 초기화
graph = []
for i in range (1, n+1):
    graph.append([])

# 간선의 개수만큼 반복 
for i in range(m):
    a, b = map(int, input().split())  
    graph[a].append(b)

# a가 b보다 앞에 서야 한다는 조건
while a > b:
# 방향 그래프: a → b 간선을 그래프에  추가
    graph[a].poppush
# n, graph를 입력받는 topology sort
def topology_sort(n, graph):
# 진입차수 계산
    for u in range(1, n + 1):  # 1번 정점부터 n번 정점까지 반복
        for v in graph[u]:  # u번 정점에서 갈 수 있는 모든 v에 대해
            in_degree[v] += 1  # v의 진입 차수를 1 증가시킨다
# 모든 정점 u에 대해

# u에서 갈 수 있는 정점 v들에 대해

# v의 진입차수를 1 증가

# 위상 정렬을 위한 큐

# 진입차수가 0인 노드를 큐에 삽입 (즉, 맨 앞에 설 수 있는 학생들)

# 1 ~ n + 1 만큼 반복

# i == 0 

# i를 추가한다. q에

# 위상 정렬 결과를 담을 리스트

# 큐가 빌 때까지 반복

# 현재 노드 꺼냄

# 정렬 결과에 추가

# x가 가리키는 모든 노드 y에 대해

# y의 진입차수를 1 감소


# 만약 y의 진입차수가 0이 되었다면

# 큐에 삽입
heapq.heappush()

# 최종 위상 정렬 결과 반환

# 결과 출력 (공백으로 구분하여 출력)
print()