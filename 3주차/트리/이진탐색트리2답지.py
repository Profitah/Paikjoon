import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘림 (10,000개까지 대비)

input = sys.stdin.read 
preorder = list(map(int, input().split()))

def postorder(start, end):
    if start > end:
        return
    
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