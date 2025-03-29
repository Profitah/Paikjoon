import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n + 1)]
parent = [0] * (n + 1)

for j in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, p):
    parent[node] = p
    for neighbor in graph[node]:
        if parent[neighbor] == 0:  
            dfs(neighbor, node)

dfs(1, 0)  # 루트를 1로 지정하고 시작

for i in range(2, n + 1):
    print(parent[i])
