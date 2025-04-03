N, M= map(int, input().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += M//coin_lst[i] 
    M = M%coin_lst[i] 

print(count)