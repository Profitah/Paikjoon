def fibo_topdown_ver (n )
    if n in memo:
        return memo[n]
    memo[n] = fibo_topdown_ver(n-1, memo) + fibo_topdown_ver(n-2, memo)
    return memo[n]


def fibo_bottomup_ver (n):
    if n == 0:
        return n
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]