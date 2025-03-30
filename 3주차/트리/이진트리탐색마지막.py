import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
preorder = list(map(int, input.split())) # 전위 탐색 대상인 노드의 값과 순서를 배열에 저장

def postorder (start, end): # 전위 탐색 트리를 후위 탐색 트리로 바꾸는 함수. 인자는 start와 end
    if start > end: # 만약에 start가 end보다 클 때,
        return  # 값을 그냥 반환한다.
    root = preorder[start] # root 변수에 preorder[start] 즉, 전위탐색트리의 start 인덱스를 넣는다.

    idx = start + 1  # 왼쪽 서브트리: start에서 1인덱스 이동한 값.
    while idx <= end and preorder[idx] < root: # 지금 idx가 end 범위 안에 있고, preorder[idx] 값이 루트보다 작다면 반복해라.
        idx += 1 # idx = idx + 1
    
    # 왼쪽 서브트리 탐색
    postorder(start + 1, idx - 1)  # 루트 다음(start+1)부터, 루트보다 작은 값들 끝(idx - 1)까지

    # 오른쪽 서브트리 탐색
    postorder(idx, end)  # 루트보다 큰 값들이 시작되는 위치(idx)부터 끝(end)까지

    # 후위 순회에서는 루트를 마지막에 출력
    print(root)