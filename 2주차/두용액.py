# 투포인터 쓰지 말 것

import sys
input = sys.stdin.readline  

# 용액의 수 입력
num_liquids = int(input())

# 용액 리스트 입력받아 정렬
liquids = list(map(int, input().split()))
liquids.sort()

# 현재까지 찾은 최소 절댓값의 합
min_abs_sum = float('inf')

# 가장 0에 가까운 두 용액의 쌍
best_pair = (0, 0)

# 첫 번째 용액 선택
for first_index in range(num_liquids - 1):
    first_liquid = liquids[first_index]  # 기준 용액
    left = first_index + 1  # 두 번째 용액 시작 인덱스
    right = num_liquids - 1  # 끝 인덱스

    # 이분 탐색 시작
    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스
        total_sum = first_liquid + liquids[mid]  # 두 용액의 합

        # 절댓값이 더 작으면 최적 조합 갱신
        if abs(total_sum) < min_abs_sum:
            min_abs_sum = abs(total_sum)
            best_pair = (first_liquid, liquids[mid])

        # 0이면 최적의 조합이므로 탐색 종료
        if total_sum == 0:
            break
        # 합이 양수 → 줄여야 하므로 오른쪽 포인터 줄임
        elif total_sum > 0:
            right = mid - 1
        # 합이 음수 → 키워야 하므로 왼쪽 포인터 올림
        else:
            left = mid + 1

# 결과 출력
print(*best_pair)
