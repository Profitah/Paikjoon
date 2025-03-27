import sys
input = sys.stdin.readline

N = int(input()) # 정수 n을 입력받고
tree = {} # tree 딕셔너리를 생성한다.

# 트리 구성: 딕셔너리로 저장
for i in range(N): # n만큼 반복하여
    root, left, right = input().strip().split()  #root, left, right 값을 한 줄에 입력하고 
    tree[root] = [left, right] # tree딕셔너리에 root key를 매칭한 뒤, left right 값을 준다.

# 전위 순회: 루트 → 왼쪽 → 오른쪽
def preorder(node): # node를 인자로 받는 preorder 함수 
    if node == '.': # 만약 node 값이 "." 이라면 
        return # 반환한다.
    print(node, end='') # 그리고 출력한다. node뒤에 개행문자 없이 
    preorder(tree[node][0]) # node는 딕셔너리(tree) 의 key | tree[node]는 자식 2개를 담은 리스트 (왼쪽, 오른쪽 순서) | tree[node][0]는 그 중 왼쪽 자식 노드 | tree[node][1]는 오른쪽 자식 노드
    preorder(tree[node][1]) #  node는 딕셔너리(tree) 의 key | tree[node]는 자식 2개를 담은 리스트 (왼쪽, 오른쪽 순서) | tree[node][0]는 그 중 왼쪽 자식 노드 | tree[node][1]는 오른쪽 자식 노드

# 중위 순회: 왼쪽 → 루트 → 오른쪽
def inorder(node): # node를 인자로 받는 inorder 함수.
    if node == '.': # node 값이 "." 일때
        return # 반환한다.
    inorder(tree[node][0]) # inorder함수를 사용한다. (이것은 재귀호출이다.) tree의 key node의 자식 리스트에서 0번째 자식에.
    print(node, end='') # node를 출력한다. 옆에(아래) 개행문자 없애고
    inorder(tree[node][1]) # inorder (이것은 재귀호출이다.)

# 후위 순회: 왼쪽 → 오른쪽 → 루트
def postorder(node): # node를 인자로 받는 postorder 함수.
    if node == '.': # node의 값이 .이 되면, 
        return # 반환한다.
    postorder(tree[node][0]) # tree 딕셔너리 node 키의 0번째 자식에 재귀함수를 사용하고 
    postorder(tree[node][1]) # tree 딕셔너리 node 키의 1번째 자식에 재귀함수를 사용하고 
    print(node, end='') # 개행문자 없이 노드를 출력하여 

# 실행
preorder('A')  # 이 줄에서 출력: ABDCEFG
print()        # 줄 바꿈

inorder('A')   # 출력: DBAECFG
print()        # 줄 바꿈

postorder('A') # 출력: DBEGFCA