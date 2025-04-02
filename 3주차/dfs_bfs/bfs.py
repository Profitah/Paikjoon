from collections import deque  # deque는 큐(Queue)를 빠르게 구현하기 위한 자료구조입니다.

# BFS(너비 우선 탐색) 함수 정의
def bfs(graph, start, visited): 
    queue = deque([start])      # 시작 노드를 큐에 넣고 시작합니다.
    visited[start] = True       # 시작 노드를 방문했다고 표시합니다.

    while queue:                # 큐가 빌 때까지 반복합니다.
        v = queue.popleft()     # 큐에서 가장 앞에 있는 노드를 꺼냅니다.
        print(v, end=' ')       # 꺼낸 노드를 출력합니다.

        # 현재 노드 v와 연결된 모든 인접 노드들을 확인합니다.
        for i in graph[v]:
            if not visited[i]:        # 만약 아직 방문하지 않은 노드라면
                queue.append(i)       # 큐에 넣어 다음에 방문하도록 준비하고
                visited[i] = True     # 방문했다고 표시합니다.

# 그래프를 인접 리스트 방식으로 정의합니다.
# 노드 번호가 1번부터 시작하므로, 0번 인덱스는 비워둡니다.
graph = [
    [],         # 0번 노드 (사용하지 않음)
    [2, 3],     # 1번 노드는 2번, 3번과 연결되어 있음
    [1, 4, 5],  # 2번 노드는 1, 4, 5번과 연결되어 있음
    [1],        # 3번 노드는 1번과 연결되어 있음
    [2],        # 4번 노드는 2번과 연결되어 있음
    [2]         # 5번 노드는 2번과 연결되어 있음
]

visited = [False] * 6  # 총 6개의 노드(0번~5번)를 위한 방문 리스트. 처음엔 모두 미방문(False)

bfs(graph, 1, visited)  # 1번 노드부터 BFS 탐색 시작