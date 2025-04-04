n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

ans = 0

# 가장 큰 동전부터 사용하기 위해 역순으로 반복
for i in range(n - 1, -1, -1):
    ans += k // coins[i]  # 해당 동전 몇 개 쓸 수 있는지
    k %= coins[i]         # 남은 금액 갱신

print(ans)