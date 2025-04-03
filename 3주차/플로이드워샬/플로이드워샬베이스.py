INF = int(1e9)  # 무한을 의미하는 값 (1억)

# 노드 개수 (예: 4개)
n = 4

# 2차원 리스트(그래프) 생성 및 초기화
graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력 (예시)
edges = [
    (1, 2, 4),
    (1, 4, 6),
    (2, 1, 3),
    (2, 3, 7),
    (3, 1, 5),
    (3, 4, 4),
    (4, 3, 2)
]

for a, b, c in edges:
    graph[a][b] = c  # a에서 b로 가는 비용은 c

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):           # 거쳐갈 노드
    for i in range(1, n + 1):       # 출발 노드
        for j in range(1, n + 1):   # 도착 노드
            # i에서 j로 가는 거리 vs i -> k -> j로 가는 거리 비교
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()