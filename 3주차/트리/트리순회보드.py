# 스택을 사용한 전위순회
import sys
input = sys.stdin.readline

N = int(input())
tree = {} # 딕셔너리를 사용한 구현

for i in range(N): # N번 동안
    root, left, right = input().strip().split() # root, left, right를 공백없이 입력받아라
    tree[root] = [left, right] # tree의 키값은 root, 거기에 left와 right를 입력받아라 

def preorder_stack(start): # start 
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node == '.':
            continue
        result.append(node)
        stack.append(tree[node][1]) 
        stack.append(tree[node][0])  
    return ''.join(result)

def inorder(node):
    if node == '.':
        return ''
    return inorder(tree[node][0]) + node + inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return ''
    return postorder(tree[node][0]) + postorder(tree[node][1]) + node

print(preorder_stack('A'))
print(inorder('A'))
print(postorder('A'))