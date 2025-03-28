import sys 
from collections import deque 

input = sys.stdin.readline  #sys.stdin.readline

# 입력 받기
node, line, start = map(int, input().split())

# 인접 행렬 생성 (노드 번호는 1부터 시작)
arr = [[0] * (node + 1) for _ in range(node + 1)]
check = [False] * (node + 1)

# 간선 정보 입력
for _ in range(line):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1  # 무방향 그래프

# DFS 함수 정의
def dfs(v):
    check[v] = True
    print(v, end=' ')
    
    for i in range(1, node + 1):  # 1부터 node까지 순회
        if arr[v][i] == 1 and not check[i]:
            dfs(i)

# BFS 함수 정의
def bfs(v):
    queue = deque([v])
    check[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        
        for i in range(1, node + 1):
            if arr[now][i] == 1 and not check[i]:
                queue.append(i)
                check[i] = True

# 실행
dfs(start)
print()
check = [False] * (node + 1)  # 방문 기록 초기화
bfs(start)
