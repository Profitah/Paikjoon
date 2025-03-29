N = int(input()) 
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, current, p, m, mu, d):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    if p:
        dfs(idx + 1, current + A[idx], p - 1, m, mu, d)
    if m:
        dfs(idx + 1, current - A[idx], p, m - 1, mu, d)
    if mu:
        dfs(idx + 1, current * A[idx], p, m, mu - 1, d)
    if d:
        if current < 0:
            dfs(idx + 1, -(-current // A[idx]), p, m, mu, d - 1)
        else:
            dfs(idx + 1, current // A[idx], p, m, mu, d - 1)

dfs(1, A[0], plus, minus, mul, div)
print(max_val)
print(min_val)
