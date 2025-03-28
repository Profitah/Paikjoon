import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘림 (10,000개까지 대비)

input = sys.stdin.readline
preorder = list(map(int, input().split())) # 전위 순회를 위해 노드값 입력받기

def postorder(start, end): # 후위 순회 함수
    if start > end: # 종료 조건
        return # 재귀 탈출
    root = preorder[start]
    # 왼쪽 서브트리: root보다 작은 값
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1
    # 왼쪽 부분 탐색
    postorder(start + 1, idx - 1)
    # 오른쪽 부분 탐색
    postorder(idx, end)
    # 마지막에 루트 출력
    print(root)
postorder(0, len(preorder) - 1)