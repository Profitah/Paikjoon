import sys
input = sys.stdin.readline

N = input.split()
tree = {}
 
for N in range(N):
    root, left, right = input.strip()
    tree[root] = [left, right]

def preorder(root):
    if root and root != "."	:
        print(root , end="")

def inorder(root):
    if root and root != "."	:
        print(root, end='')  
        inorder(tree[root][0])  
        inorder(tree[root][1])  
 
def postorder(root):
    if root and root != "."	:
        print(root, end='') 
        postorder(tree[root][0]) 
        postorder(tree[root][1])

preorder('A')
print()
inorder('A')
print()
postorder('A')

