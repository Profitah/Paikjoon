import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘림 (10,000개까지 대비)

input = sys.stdin.readline
preorder = list(map(int, input().split())) 

def postorder(start, end): # 전위 탐색 트리를 후위 탐색 트리로 바꾸는 함수. 인자는 start와 end
    if start > end: # 만약에 start가 end보다 클 때,
        return # 값을 그냥 반환한다.
    
    root = preorder[start] 
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1
        
    # 왼쪽 서브트리 탐색
    postorder(start + 1, idx - 1)  # 루트 다음(start+1)부터, 루트보다 작은 값들 끝(idx - 1)까지
    # 오른쪽 서브트리 탐색
    postorder(idx, end)  # 루트보다 큰 값들이 시작되는 위치(idx)부터 끝(end)까지
    # 후위 순회에서는 루트를 마지막에 출력
    print(root)
postorder(0, len(preorder) - 1)
