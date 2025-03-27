import sys
input = sys.stdin.readline

N = int(input())
tree = {}

# 트리 구성: 딕셔너리로 저장
for i in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 전위 순회: 루트 → 왼쪽 → 오른쪽
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회: 왼쪽 → 루트 → 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

# 후위 순회: 왼쪽 → 오른쪽 → 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

# 실행
preorder('A')
print()
inorder('A')
print()
postorder('A')
