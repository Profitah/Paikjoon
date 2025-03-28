import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []
while True:
    try:
        a = int(input())
        graph.append(a)
    except:
        break

###########################################################

#트리를 튜플형태로 저장하는 방법
def LAB_tree_tuple(graph): 
    if not graph:
        return None

    root = graph[0]

    # 왼쪽 하위 트리와 오른쪽 하위 트리로 나눈다.
    left_subtree = [x for x in graph if x < root]
    right_subtree = [x for x in graph if x > root]

    left = LAB_tree_tuple(left_subtree)
    right = LAB_tree_tuple(right_subtree)

    return (root, left, right)

#트리를 딕셔너리 형태로 저장하는 방법
def LAB_tree_diction(graph):
    if not graph:
        return None

    root = graph[0]

    # 왼쪽 하위 트리와 오른쪽 하위 트리로 나눈다.
    left_subtree = [x for x in graph if x < root]
    right_subtree = [x for x in graph if x > root]

    left = LAB_tree_diction(left_subtree)
    right = LAB_tree_diction(right_subtree)

    return {"root": root, "left": left, "right": right}

###########################################################     

#전위순회
def LAB(tree):
    result = []
    if tree:
        result.append(tree["root"])
        result.extend(ABL(tree["left"]))
        result.extend(ABL(tree["right"]))
    return result   

#중위순회
def ALB(tree):
    result = []
    if tree:
        result.extend(ABL(tree["left"]))
        result.append(tree["root"])
        result.extend(ABL(tree["right"]))
    return result

#후위순회
def ABL(tree):
    result = []
    if tree:
        result.extend(ABL(tree["left"]))
        result.extend(ABL(tree["right"]))
        result.append(tree["root"])
    return result           

###########################################################

tree = LAB_tree_diction(graph)
result_list = ABL(tree)

for i in range(len(result_list)):
    print(result_list[i])