import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용
n, m = map(int, input().split())  # 학생 수 n, 정보 수 m 입력 받음
graph = [[] for i in range(n + 1)]  # 학생 번호가 1번부터 시작하므로 n+1 크기로 그래프 초기화

for i in range(m): # m 만큼 
    a, b = map(int, input().split())  # a가 b보다 앞에 서야 한다는 조건
    graph[a].append(b)  # 방향 그래프: a → b 간선 추가

def topologySort(n, graph): # n, graph를 입력받는 topology sort
    in_degree = [0] * (n + 1)  # 각 노드의 진입차수(앞에 있어야 하는 학생 수) 저장 배열

    # 진입차수 계산
    for u in range(1, n + 1):         # 모든 정점 u에 대해
        for v in graph[u]:            # u에서 갈 수 있는 정점 v들에 대해
            in_degree[v] += 1         # v의 진입차수를 1 증가

    q = deque()  # 위상 정렬을 위한 큐

    # 진입차수가 0인 노드를 큐에 삽입 (즉, 맨 앞에 설 수 있는 학생들)
    for i in range(1, n + 1): # 1 ~ n + 1 만큼 반복
        if in_degree[i] == 0: # i == 0 
            q.append(i) # i를 추가한다. 배열 q에

    result = []  # 위상 정렬 결과를 담을 리스트

    while q:  # 큐가 빌 때까지 반복
        x = q.popleft()     # 현재 노드 꺼냄
        result.append(x)    # 정렬 결과에 추가

        for y in graph[x]:  # x가 가리키는 모든 노드 y에 대해
            in_degree[y] -= 1        # y의 진입차수를 1 감소
            if in_degree[y] == 0:    # 만약 y의 진입차수가 0이 되었다면
                q.append(y)          # 큐에 삽입

    return result  # 최종 위상 정렬 결과 반환

print(*topologySort(n, graph))  # 결과 출력 (공백으로 구분하여 출력)