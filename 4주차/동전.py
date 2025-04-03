n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

ans = 0

for i in range(n - 1, -1, -1):
    ans += k // coins[i]  
    k %= coins[i]         

print(ans)

https://puleugo.tistory.com/20