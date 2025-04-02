def dfs(graph, v, visited): # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')  # 방문한 노드 출력

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드라면 재귀 호출
            dfs(graph, i, visited)

# 예제 그래프 (0번 노드는 사용하지 않음)
graph = [
    [],          # 0번 노드는 사용 안 함
    [2, 3, 4],   # 1번 노드와 연결된 노드들
    [1, 5],      # 2번 노드와 연결된 노드들
    [1, 6, 7],   # 3번 노드와 연결된 노드들
    [1, 8],      # 4번 노드와 연결된 노드들
    [2],         # 5번 노드
    [3],         # 6번 노드
    [3],         # 7번 노드
    [4]          # 8번 노드
]

# 방문 리스트 (False로 초기화)
visited = [False] * len(graph)

# DFS 실행 (1번 노드부터 시작)
dfs(graph, 1, visited)
