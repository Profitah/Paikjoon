import sys

def get_smallest_node(distance, visited):
    """ 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 찾기 """
    min_value = float('inf')
    index = 0  # 최단 거리 노드의 인덱스
    
    for i in range(1, len(distance)):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(graph, start):
    """ 다익스트라 알고리즘 (일반 리스트 사용) """
    n = len(graph)
    INF = float('inf')
    
    # 최단 거리 테이블 초기화
    distance = [INF] * n
    visited = [False] * n
    
    # 시작 노드 거리 0으로 설정
    distance[start] = 0

    # 모든 노드 확인 (총 V번 반복)
    for _ in range(n - 1):
        now = get_smallest_node(distance, visited)  # 방문하지 않은 노드 중 최단 거리 노드 선택
        visited[now] = True  # 방문 처리

        # 현재 노드와 연결된 노드의 거리 갱신
        for neighbor, weight in graph[now]:
            cost = distance[now] + weight
            if cost < distance[neighbor]:  # 더 짧은 경로를 찾으면 업데이트
                distance[neighbor] = cost

    return distance

# 예제 그래프 (인접 리스트 방식)
graph = [
    [],  # 0번 노드는 사용 안 함
    [(2, 2), (3, 5), (4, 1)],  # 1번 노드
    [(1, 2), (3, 3), (4, 2)],  # 2번 노드
    [(1, 5), (2, 3), (4, 3), (5, 1)],  # 3번 노드
    [(1, 1), (2, 2), (3, 3), (5, 1)],  # 4번 노드
    [(3, 1), (4, 1)]  # 5번 노드
]

# 다익스트라 실행 (1번 노드에서 시작)
start_node = 1
shortest_distances = dijkstra(graph, start_node)

# 결과 출력
for i in range(1, len(shortest_distances)):
    print(f"노드 {i}까지의 최단 거리: {shortest_distances[i]}")
