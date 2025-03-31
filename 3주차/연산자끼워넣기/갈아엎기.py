# 입력: 숫자의 개수 N
N = int(input())

# 수열 입력: N개의 숫자
numbers = list(map(int, input().split()))

# 연산자 개수 입력: +, -, *, // 순서로 각각 개수
plus, minus, multiply, divide = map(int, input().split())

# 결과 저장용 리스트: [최댓값, 최솟값]
# 초기값은 -1e9(작은 수), 1e9(큰 수)로 설정
result = [-1e9, 1e9]

# DFS 함수 정의
def dfs(idx, current_value, plus, minus, multiply, divide, result):
    # idx: 현재 처리할 numbers 인덱스
    # current_value: 지금까지의 계산 결과
    # plus~divide: 남은 연산자의 수
    # result: 최댓값과 최솟값을 담는 리스트

    # 기저 조건: 모든 숫자를 다 사용했다면 결과 갱신 후 종료
    if idx == N:
        result[0] = max(result[0], current_value)  # 최댓값 갱신
        result[1] = min(result[1], current_value)  # 최솟값 갱신
        return

    # 다음 숫자
    next_number = numbers[idx]

    # 덧셈 연산자가 남아 있으면 덧셈 수행 후 재귀 호출
    if plus > 0:
        dfs(idx + 1, current_value + next_number, plus - 1, minus, multiply, divide, result)

    # 뺄셈
    if minus > 0:
        dfs(idx + 1, current_value - next_number, plus, minus - 1, multiply, divide, result)

    # 곱셈
    if multiply > 0:
        dfs(idx + 1, current_value * next_number, plus, minus, multiply - 1, divide, result)

    # 나눗셈 (주의: 음수 나눗셈은 C++14 방식으로 처리)
    if divide > 0:
        if current_value < 0:
            # 음수면 절댓값으로 나눈 뒤 부호 다시 씌움
            dfs(idx + 1, -(-current_value // next_number), plus, minus, multiply, divide - 1, result)
        else:
            dfs(idx + 1, current_value // next_number, plus, minus, multiply, divide - 1, result)

# DFS 시작 (첫 숫자는 고정이므로 index 1부터 탐색 시작)
dfs(1, numbers[0], plus, minus, multiply, divide, result)

# 최댓값 출력
print(int(result[0]))

# 최솟값 출력
print(int(result[1]))
