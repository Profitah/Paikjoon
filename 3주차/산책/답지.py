import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1. 입력
N = int(input())  # 장소 수 (노드 수)
room_str = input().strip()  # 실내/실외 정보 
A = list(map(int, room_str))  # 문자열을 정수 리스트로 변환

# 2. 그래프 초기화
graph = []
for i in range(N):
    graph.append([]) 
    u, v = map(int, input().split())
    u -= 1  # 인덱스 보정 (1 → 0부터 시작)
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 3. 방문 배열
visited = [False] * N

# 4. 실외 노드에서 연결된 실내 노드 수를 세는 DFS 함수
def dfs(node):
    visited[node] = True
    cnt = 0
    for neighbor in graph[node]:
        if A[neighbor] == 1:
            cnt += 1
        elif not visited[neighbor] and A[neighbor] == 0:
            cnt += dfs(neighbor)
    return cnt

# 5. 정답 계산
answer = 0

# (1) 실내 - 실내 직접 연결된 간선 세기
for i in range(N):
    if A[i] == 1:
        for j in graph[i]:
            if A[j] == 1:
                answer += 1

# (2) 실외 노드 DFS 탐색 → 실내 노드끼리 짝지을 수 있는 경우의 수 계산
for i in range(N):
    if A[i] == 0 and not visited[i]:
        cnt = dfs(i)
        answer += cnt * (cnt - 1)

# (3) 실내 ↔ 실내 간선은 중복으로 셌으므로 절반으로 나눔
print(answer // 2)