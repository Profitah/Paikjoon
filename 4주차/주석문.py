# n: 동전의 종류 수, k: 만들어야 하는 금액
n, k = map(int, input().split())

# 각 동전의 가치를 저장할 리스트
coins = []

# 동전 가치 입력 받기
for i in range(n):
    coins.append(int(input()))

# 사용한 동전 개수를 저장할 변수
ans = 0

# 큰 동전부터 사용하기 위해 리스트의 끝에서부터 역순으로 탐색
for i in range(n - 1, -1, -1):
    # 현재 동전으로 만들 수 있는 최대 개수를 더함
    ans += k // coins[i]

    # 해당 동전을 사용하고 남은 금액으로 갱신
    k %= coins[i]

# 정답(사용한 동전의 최소 개수) 출력
print(ans)


피보나치를 바텀업으로 구현.
0일때와 1일때 조건 필요


i = 2, 3, 4
dp 2= dp 0 + dp 1

