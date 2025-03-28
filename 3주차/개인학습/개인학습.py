inorder('A') 호출

현재 노드: 'A'
왼쪽 자식 노드: 'B'
inorder('B') 호출
inorder('B') 호출

현재 노드: 'B'
왼쪽 자식 노드: 'D'
inorder('D') 호출
inorder('D') 호출

현재 노드: 'D'
왼쪽 자식 노드가 없으므로 return (D 출력)
inorder('B')로 돌아와서 'B' 출력

오른쪽 자식 노드: 'E'
inorder('E') 호출
inorder('E') 호출

현재 노드: 'E'
왼쪽 자식 노드가 없으므로 return (E 출력)



def preorder(node): # node를 인자로 받는 preorder 함수 
    if node == '.': # 만약 node 값이 "." 이라면 
        return # 그대로 반환한다.
    print(node, end='') # 그리고 출력한다. node뒤에 개행문자 없이 
    preorder(tree[node][0]) # 함수 실행 범위
    preorder(tree[node][1]) # 힘수 실행 범위