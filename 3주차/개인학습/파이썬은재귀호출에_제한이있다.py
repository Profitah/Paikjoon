import sys  # 시스템 관련 모듈 불러오기 (입력, 재귀 설정 등)
sys.setrecursionlimit(10**6)  # 파이썬의 기본 재귀 깊이 제한(1000)을 100만까지 확장
# → 깊은 트리를 탐색할 때 RecursionError 방지
input = sys.stdin.readline  # 빠른 입력을 위한 sys.stdin.readline 사용 (백준에서 권장)
preorder = []  # 전위 순회된 이진 검색 트리 데이터를 저장할 리스트
# 입력 받기 (EOF가 나올 때까지 무한히 입력 받음)
while True:
    try:
        preorder.append(int(input()))  # 한 줄씩 정수를 읽어 preorder 리스트에 저장
    except:
        break  
    
# 후위 순회를 수행하는 재귀 DFS 함수 정의
def dfs(start, end):  # start: 현재 서브트리 시작 인덱스, end: 끝 인덱스
    if start > end:  # 잘못된 범위이거나 리프 노드 처리 완료 시
        return  # 함수 종료

    root = preorder[start]  # 전위 순회에선 첫 번째 값이 항상 루트 노드
    idx = start + 1  # 오른쪽 서브트리 시작 인덱스를 찾기 위해 초기화
    while idx <= end and preorder[idx] < root: # 왼쪽 서브트리: root보다 작은 값들 → 오른쪽 서브트리 시작점 찾기
        idx += 1

    # 왼쪽 서브트리에 대해 재귀 호출
    dfs(start + 1, idx - 1)

    # 오른쪽 서브트리에 대해 재귀 호출
    dfs(idx, end)

    # 후위 순회이므로 루트를 마지막에 출력
    print(root)

# DFS 탐색 시작: 전체 트리 구간(0부터 N-1)으로 탐색 시작
dfs(0, len(preorder) - 1)


"""

1. 트리는 그래프의 한 종류다
그래프(Graph): 정점(vertex)과 간선(edge)으로 이루어진 자료구조

트리(Tree): 그래프의 일종, 다음 조건을 만족하는 그래프

사이클이 없음 (acyclic)

모든 노드가 연결됨 (connected)

한 노드에서 출발하면 유일한 경로로 다른 노드에 도달 가능

즉,
✅ 트리는 "방향 비순환 그래프 (DAG)"의 특별한 케이스예요.
➡️ 그래서 이진 트리 문제도 그래프 이론 문제로 분류됩니다.
"""