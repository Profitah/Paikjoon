import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = []
    if left != '.':
        tree[root].append(left)
    else:
        tree[root].append(None)
    if right != '.':
        tree[root].append(right)
    else:
        tree[root].append(None)

# 전위 순회 (루트 → 왼쪽 → 오른쪽)
def preorder(node):
    if node is None:
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회 (왼쪽 → 루트 → 오른쪽)
def inorder(node):
    if node is None:
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

# 후위 순회 (왼쪽 → 오른쪽 → 루트)
def postorder(node):
    if node is None:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

# 루트는 항상 A로 시작 (문제 조건)
preorder('A')
print()
inorder('A')
print()
postorder('A')
