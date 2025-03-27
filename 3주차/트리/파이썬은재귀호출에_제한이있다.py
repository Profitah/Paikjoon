import sys  # 시스템 관련 기능을 사용하기 위한 모듈 import
print(sys.getrecursionlimit())  # 현재 파이썬의 재귀 호출 깊이 제한을 출력 (기본값은 1000)
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 1,000,000으로 확장 (깊은 트리 구조를 위한 설정) # 파이썬 재귀호출은 제한범위가 있으므로 
input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline 사용

preorder = []  # 전위 순회로 주어지는 노드들을 저장할 리스트 초기화

# 입력 받기
while True:  # 무한 루프를 돌며 입력을 계속 받는다
    try:  # 예외가 발생하지 않는다면
        preorder.append(int(input()))  # 입력 값을 정수로 변환해서 preorder 리스트에 추가
    except:  # 입력이 끝나거나 예외가 발생하면
        break  # 반복 종료

# 후위 순회를 위한 DFS 함수 정의
def dfs(pl, pr):  # pl: 시작 인덱스, pr: 끝 인덱스 (preorder 리스트의 구간을 의미)
    if pl > pr:  # 시작이 끝보다 크면 잘못된 구간이므로
        return  # 함수를 종료한다

    root = preorder[pl]  # 현재 구간의 루트 노드는 맨 앞에 있는 값
    idx = pl + 1  # 오른쪽 서브트리를 찾기 위한 시작 인덱스 초기화

    # 루트보다 큰 값이 나올 때까지 idx를 증가시킴 → 오른쪽 서브트리 시작 위치 찾기
    while idx <= pr and preorder[idx] < root:
        idx += 1  # idx를 오른쪽으로 한 칸씩 이동

    dfs(pl + 1, idx - 1)  # 왼쪽 서브트리 탐색 (pl+1부터 idx-1까지)
    dfs(idx, pr)  # 오른쪽 서브트리 탐색 (idx부터 pr까지)
    print(root)  # 후위 순회: 왼쪽 → 오른쪽 → 루트 → 루트를 마지막에 출력

# DFS 실행 (전체 범위에서 탐색 시작)
dfs(0, len(preorder) - 1)  # preorder 리스트 전체 범위를 넘겨서 트리 구성 및 출력 시작


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

