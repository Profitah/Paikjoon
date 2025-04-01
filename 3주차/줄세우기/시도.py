import sys
from collections import deque 

input = sys.stdin.readline
n, m = map(int, input().split())  # 정점의 수 n과 간선의 수 m을 입력받는다

graph = []  # 그래프를 저장할 2차원 리스트 생성
for i in range(n + 1):  # 정점 번호가 1부터 시작하므로 n+1개의 빈 리스트를 만든다
    graph.append([]) # 리스트 graph에 []을 넣는다.

for i in range(m):  # 간선의 개수만큼 반복
    a, b = map(int, input().split())  # a번 정점에서 b번 정점으로 향하는 간선 정보 입력
    graph[a].append(b)  # a에서 b로 가는 간선을 그래프에 추가

def topologySort(n, graph):  # 위상 정렬 함수 정의
    in_degree = [0] * (n + 1)  # 각 정점의 진입 차수를 저장할 리스트

    # 진입 차수 계산
    for u in range(1, n + 1):  # 1번 정점부터 n번 정점까지 반복
        for v in graph[u]:  # u번 정점에서 갈 수 있는 모든 v에 대해
            in_degree[v] += 1  # v의 진입 차수를 1 증가시킨다

    q = deque()  # 진입 차수가 0인 노드를 저장할 큐

    for i in range(1, n + 1):  # 모든 정점에 대해
        if in_degree[i] == 0:  # 진입 차수가 0이면
            q.append(i)  # 큐에 추가한다

    result = []  # 위상 정렬 결과를 저장할 리스트

    while q:  # 큐가 빌 때까지 반복
        x = q.popleft()  # 큐에서 하나 꺼냄
        result.append(x)  # 결과 리스트에 추가

        for y in graph[x]:  # x와 연결된 모든 y에 대해
            in_degree[y] -= 1  # y의 진입 차수를 1 감소시키고
            if in_degree[y] == 0:  # 진입 차수가 0이 되면
                q.append(y)  # 큐에 추가

    return result  # 위상 정렬 결과 반환

print(*topologySort(n, graph))  # 결과를 공백으로 구분하여 출력
