# index error

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # 실내/실외 정보
graph = [[] for i in range(N)]
visited = [False] * N

# 간선 입력 (N - 1개의 간선이 주어진다고 가정)
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    cnt = 0
    for neighbor in graph[node]:
        if A[neighbor] == 1:
            cnt += 1
        elif not visited[neighbor] and A[neighbor] == 0:
            cnt += dfs(neighbor)
    return cnt

answer = 0

# 실내-실내 연결
for i in range(N):
    if A[i] == 1:
        for j in graph[i]:
            if A[j] == 1:
                answer += 1

# 실외에서 연결 가능한 실내 쌍들
for i in range(N):
    if A[i] == 0 and not visited[i]:
        cnt = dfs(i)
        answer += cnt * (cnt - 1)

print(answer // 2)