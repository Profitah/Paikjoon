import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정
input = sys.stdin.readline  # 빠른 입력 처리

def dfs(node):  # DFS 함수 정의
    visited[node] = True  # 현재 노드 방문 처리

    for neighbor in graph[node]:  # 인접한 노드들 순회
        if group[neighbor] is None:  # 그룹이 아직 지정되지 않았다면
            group[neighbor] = not group[node]  # 현재 노드와 반대 그룹으로 지정
            dfs(neighbor)  # 재귀적으로 다음 노드 탐색
        elif group[neighbor] == group[node]:  # 인접 노드가 같은 그룹이면 이분 그래프 아님
            global bipartite  # 전역 변수 사용
            bipartite = False  # 이분 그래프 아님 표시
            return  # 탐색 중단

k = int(input())  # 테스트 케이스 수 입력

for i in range(k): # 각 테스트 케이스에 대해 반복   
    v_cnt, u_cnt = map(int, input().split())  # 정점 수, 간선 수 입력

    graph = []  # 인접 리스트 초기화
    for i in range(v_cnt + 1):  # 정점 번호는 1부터 v_cnt까지 사용
        graph.append([])  # 각 정점마다 빈 리스트 준비

    visited = [False] * (v_cnt + 1)  # 방문 여부 배열 초기화
    group = [None] * (v_cnt + 1)  # 각 정점의 그룹 정보 저장 (None: 아직 없음)

    bipartite = True  # 이분 그래프 여부 저장 변수 (초기값: True)

    for i in range(u_cnt):  # 간선 입력
        u, v = map(int, input().split())  # 양 끝 정점 번호 입력
        graph[u].append(v)  # u → v 연결
        graph[v].append(u)  # v → u 연결 (무방향)

    for i in range(1, v_cnt + 1):  # 1번 정점부터 v_cnt번 정점까지
        if not visited[i]:  # 아직 방문하지 않은 정점이면
            group[i] = True  # 초기 그룹을 True로 지정
            dfs(i)  # DFS 시작

        if not bipartite:  # DFS 도중 이분 그래프 아님이 판별되면
            break  # 탐색 중단

    if bipartite:  # 최종 결과에 따라 출력
        print("YES") # 이분 그래프이면 "YES" 출력
    else:
        print("NO")