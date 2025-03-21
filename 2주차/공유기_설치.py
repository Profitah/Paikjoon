
N, C = map(int, input().split()) # 입력: 집 개수 N, 공유기 개수 C
houses = [int(input()) for i in range(N)] # 집 좌표 입력받기
houses.sort()  # 좌표 오름차순 정렬 (필수)

# 공유기를 특정 거리 이상으로 설치할 수 있는지 확인하는 함수
def can_install(distance): # 거리가 주어졌을 때 공유기를 설치할 수 있는지 확인하는 함수
    count = 1              # 첫 번째 집에는 항상 설치
    last_installed = houses[0] # 마지막으로 공유기를 설치한 집

    for i in range(1, N): # 모든 집에 대해 반복
        if houses[i] - last_installed >= distance: # 이전 집과의 거리가 주어진 거리 이상이면
            count += 1 # 공유기 설치
            last_installed = houses[i] # 설치된 집 갱신

    return count >= C  # 공유기 C개 이상 설치 가능하면 True

# 이진 탐색 범위 설정
left = 1                                 # 최소 거리 (공유기 간 거리 최소값)
right = houses[-1] - houses[0]           # 최대 거리 (가장 먼 두 집 사이 거리)
answer = 0

# 이진 탐색 시작
while left <= right:
    mid = (left + right) // 2  # 현재 시도하는 거리

    if can_install(mid):
        answer = mid           # 설치 가능하면 거리 저장하고
        left = mid + 1         # 더 넓은 거리로도 가능한지 탐색
    else:
        right = mid - 1        # 설치 불가능 → 거리를 좁힘

# 결과 출력: 가장 인접한 두 공유기 사이의 최대 거리
print(answer)
