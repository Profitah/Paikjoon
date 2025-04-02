import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정 (기본 제한 초과 방지)
input = sys.stdin.readline  # 빠른 입력을 위한 설정

n = int(input())  # 정점(장소)의 개수 입력 받기
A = input().rstrip()  # 실내/실외 정보 입력 받기 ('1': 실내, '0': 실외) #rstrip()으로 개행 문자 제거

graph = []  # 그래프 인접 리스트 (초기화) ← 오류 있음, 아래에서 수정 필요

place = [0] * (n + 1)  # 장소 정보 저장용 배열 (1번부터 시작)
visited = [0] * (n + 1)  # 방문 여부 저장 배열 (1번부터 시작)

for i in range(n):  # n개의 장소 정보를 읽어서
    place[i + 1] = int(A[i])  # 1-based index로 실내/실외 정보 저장

graph = [[] for _ in range(n + 1)]  # 각 정점의 인접 리스트를 위한 그래프 초기화

for i in range(n - 1):  # n - 1개의 간선을 입력 받아
    a, b = map(int, input().split())  # a, b 정점 번호 입력
    graph[a].append(b)  # 양방향 간선 추가 (a → b)
    graph[b].append(a)  # 양방향 간선 추가 (b → a)

def dfs(node):  # DFS 함수 정의 (현재 정점 기준)
    count = 0  # 연결된 실내 노드 수 세기
    for neighbor in graph[node]:  # 인접한 모든 노드에 대해
        if place[neighbor] == 1:  # 이웃이 실내라면
            count += 1  # 유효 경로 1개 증가
        elif not visited[neighbor]:  # 이웃이 실외면서 아직 방문 안 했다면
            visited[neighbor] = 1  # 방문 처리
            count += dfs(neighbor)  # 재귀 DFS로 탐색 계속
    return count  # 해당 컴포넌트에서 연결된 실내 노드 수 반환

answer = 0  # 정답(총 경로 수)을 저장할 변수

# 실내-실내 직접 연결된 경우를 탐색
for i in range(1, n + 1):
    if place[i] == 1:  # i번 노드가 실내라면
        for visit in graph[i]:  # 인접 노드들 중
            if place[visit] == 1:  # 이웃도 실내라면
                answer += 1  # 경로 1개 추가 (양쪽에서 두 번 세지만 나중에 따로 처리 안 함)

# 실외를 통해 연결된 실내 노드 쌍 계산
for i in range(1, n + 1):
    if place[i] == 0 and not visited[i]:  # 실외이면서 아직 방문하지 않았다면
        visited[i] = 1  # 방문 처리
        count = dfs(i)  # DFS로 연결된 실내 노드 수 확인
        answer += count * (count - 1)  # 실내 노드 쌍의 수 = 조합 countC2 = count * (count - 1)

print(answer)  # 정답 출력
