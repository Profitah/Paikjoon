# 입력
# 이진 탐색으로 풀이 필요
# 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
N, M = map(int, input().split()) # 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M

tree = list(map(int, input().split()))  # `N`개의 나무를 리스트로 받음

# 이진 탐색 사용을 위한 준비
tree.sort() # 이진 탐색을 수행하기 위해서는 반드시 정렬해야함.

# 출력
# 이진 탐색을 이용한 풀이
def tree_cutting(M, tree): 

    # 초기화 설정
    pl = 0 # 절단기의 최소 높이
    pr = max(tree) 
    cursor = (pl + pr) // 2  # 현재 탐색할 중앙값 (pc)

    # 탐색 범위가 유효한 동안 반복
    while pl <= pr: # 
        cursor = (pl + pr) // 2  # 절단기의 높이 (중앙값)
        cut = 0  # 절단된 나무의 길이 초기화


    # 절단기로 나무를 절단하고 남은 나무의 길이를 계산
        for i in tree:
            if i > cursor:
                cut += i - cursor

    # 절단된 나무의 길이가 필요한 나무의 길이보다 작다면
        if cut < M:
            pr = cursor - 1
    # 절단된 나무의 길이가 필요한 나무의 길이보다 크다면
        else:
            pl = cursor + 1
            tree_h_king = cursor

    # 절단된 나무의 길이가 필요한 나무의 길이와 같다면
        if cut == M:

    # 절단기의 최대 높이 구하기
            return cursor
        
    return tree_h_king

if sum(tree) < M: # 나무의 길이가 부족한 경우
    print (0)  # 절단기의 최대 높이 출력
else:
    tree_h_king = tree_cutting(M, tree)
    
    # 절단기의 최대 높이 출력
    print (tree_h_king) 