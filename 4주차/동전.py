n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

result = 0

for i in range(n - 1, -1, -1):
    result += k // coins[i]  
    k %= coins[i]         

print(result)

https://puleugo.tistory.com/20