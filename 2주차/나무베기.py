# 입력
N, M = map(int, input().split()) # 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
tree = list(map(int, input().split()))  # `N`개의 나무를 리스트로 받음

# 이진 탐색 사용을 위한 준비
tree.sort() # 이진 탐색을 수행하기 위해서는 반드시 정렬해야함.

# 나무 자르기 함수
def tree_cutting(M, tree):# 이분 탐색을 실행한다. 나무의 길이에서 나무리스트의 길이 만큼을 인자로 받는다.
    pl = 0 # 나무의 최소 길이 (이분 탐색 좌측 포인터)
    pr = max(tree) # 나무의 최대 길이 (이분 탐색 우측 포인터)
    h = 0 #  가장 알맞은 절단기 높이

    while pl <= pr: # 좌측 포인터가 우측 포인터보다 작거나 같을 때까지 (탐색 범위가 남아있을 때까지)
        cursor = (pl + pr) // 2 # 중앙 값을 계산하고 (현재 시도해볼 절단기 높이(cursor)를 정한다)
        cut = 0 # 잘린 나무의 길이를 저장할 변수

        for i in tree:  # 나무 리스트에 있는 인덱스를 하나씩 순회하며
            if i > cursor: # 인덱스가 나무가 절단기보다 높으면 자르고
                cut += i - cursor  # 이때 자른 나무의 길이를 누적한다.

        if cut < M: # 잘린 길이가 목표 길이보다 작으면
            pr = cursor - 1 # False를 반환하고, 우측 포인터를 작게 설정
        elif cut > M: # 잘린 길이가 목표 길이보다 크면
            pl = cursor + 1 # True를 반환하고 , 좌측 포인터를 중앙값보다 크게 설정
            h = cursor # 나무의 높이를 저장
        else: # 그 외의 경우 
            return cursor # 중앙값을 반환하고 

    return h # 나무의 높이 반환

if sum(tree) < M: # 나무의 길이가 목표 길이보다 작으면
    print(0) # 0을 출력하고,
else: # 그게 아니라면 
    print(tree_cutting(M, tree)) # 절단기에 설정할 수 있는 최대 높이를 출력한다. 