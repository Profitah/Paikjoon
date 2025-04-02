# index error 못 고치겠음 ㅠㅠ

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  
graph = [[] for i in range(N)]

if len(A) != N:
    print("입력 오류: 실내/실외 정보 개수가 맞지 않습니다.")
    exit()


for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * N

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

for i in range(N):
    if A[i] == 1:
        for j in graph[i]:
            if A[j] == 1 and i < j:  
                answer += 1

for i in range(N):
    if A[i] == 0 and not visited[i]:
        cnt = dfs(i)
        answer += cnt * (cnt - 1)

print(answer // 2)