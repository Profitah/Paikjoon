from typing import Any, Sequence 
# 함수정의
def A에서X찾기(A: Sequence, X: Any) -> int:
    pl = 0
    pr = len(A) - 1

    while pl <= pr:

        pc = (pl + pr) // 2
    
        if A[pc] < X:
            pl = pc + 1

        elif A[pc] == X:
            return 1

        else:
            pr = pc - 1

    return 0

# 사용자 상호작용
N = int(input()) # A 리스트의 길이 
A = list(map(int, input().split())) # A 리스트의 요소들 
A.sort() # 이분탐색은 정렬된 리스트에서만 가능하므로, 정렬한다.
M = int(input()) # M 리스트의 길이
M_list = list(map(int, input().split())) # M 리스트의 요소들

# 결과 출력
for i in M_list: # M 리스트들의 요소들을 하나씩 꺼내서 
    print(A에서X찾기(A, i)) # A 리스트에서 그 요소가 있는지 확인한다. 있으면 1, 없으면 0을 출력한다.