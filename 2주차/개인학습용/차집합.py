import sys
input = sys.stdin.readline

def binary(arr, target): # 이진 탐색 함수: 정렬된 배열 arr에서 target 값이 존재하는지 확인
    # 이진 탐색 함수: 정렬된 배열 arr에서 target 값이 존재하는지 확인
    pl = 0  # 탐색 구간의 왼쪽 끝 인덱스
    pr = len(arr) - 1  # 탐색 구간의 오른쪽 끝 인덱스 (인덱스는 0부터 시작하므로 -1)

    while pl <= pr: # pl이 pr보다 작거나 같을 때까지
        pc = (pl + pr) // 2  # 중간 인덱스 계산
        if arr[pc] == target:
            return True # 찾았을 때 True 반환
        elif arr[pc] < target:
            pl = pc + 1
        else:
            pr = pc - 1
    return False  # 끝까지 찾지 못한 경우 False

# A 집합과 B 집합의 크기 입력, 각각의 원소 입력
n_a, n_b = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

# 이진 탐색을 위해 B 배열을 오름차순 정렬
arr_B.sort()

# A의 원소 중 B에 없는 것만 추려냄
result = []
for a in arr_A:
    if not binary(arr_B, a):
        result.append(a)

# 결과를 오름차순 정렬 후 출력
result.sort()
print(len(result))
if result:
    print(' '.join(map(str, result)))