import sys
input = sys.stdin.readline

# 노드의 수 입력
N = int(input().strip())
tree = {}

# 이진 트리 구성
for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])  # 왼쪽 자식
        preorder(tree[root][1])  # 오른쪽 자식

# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0])  # 왼쪽 자식
        print(root, end="")
        inorder(tree[root][1])  # 오른쪽 자식

# 후위 순회
def postorder(root):
    if root != ".":
        postorder(tree[root][0])  # 왼쪽 자식
        postorder(tree[root][1])  # 오른쪽 자식
        print(root, end="")

# 루트 노드로 순회 시작 (예: 'A'가 루트 노드라고 가정)
root_node = 'A'  # 실제 루트 노드 이름으로 변경
print("전위 순회:", end=" ")
preorder(root_node)
print()
print("중위 순회:", end=" ")
inorder(root_node)
print()
print("후위 순회:", end=" ")
postorder(root_node)
print()