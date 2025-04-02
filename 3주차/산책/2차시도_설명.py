# 다시 보니 만점이 아니여서 다시 짜야 한다.

import sys  # 시스템 관련 기능을 사용하기 위해 sys 모듈 import
sys.setrecursionlimit(10**6)  # 재귀 호출 제한을 늘려줌 (기본 제한보다 깊게 탐색 가능하도록 설정)
input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용

n = int(input())  # 정점(장소) 수 입력

room_str = input().strip()  # 실내/실외 정보 입력 (공백 제거된 문자열)
A = list(map(int, room_str))  # 각 자리의 '0' 또는 '1'을 정수형 리스트로 변환하여 저장

graph = []  # 그래프(인접 리스트) 초기화
for i in range(n + 1):  # 노드 수 + 1 만큼 반복 (1번 노드부터 사용하기 때문)
    graph.append([])  # 각 노드의 인접 리스트를 빈 리스트로 만들어 추가

for _ in range(n - 1):  # n - 1개의 간선을 입력 받음
    u, v = map(int, input().split())  # 양 끝점 입력
    u -= 1  # 문제는 1-indexed, 우리는 0-indexed로 사용
    v -= 1  # 인덱스 보정
    graph[u].append(v)  # u와 v를 서로 연결 (무방향 간선)
    graph[v].append(u)

visited = [False] * n  # 방문 여부를 저장하는 리스트 초기화 (n개의 노드)

def dfs(node):  # DFS 함수 정의
    visited[node] = True  # 현재 노드를 방문 처리
    cnt = 0  # 현재 실외 컴포넌트에서 연결된 실내 노드 수
    for neighbor in graph[node]:  # 인접한 노드들 순회
        if A[neighbor] == 1:  # 실내 노드라면
            cnt += 1  # 유효한 실내 노드 수 증가
        elif not visited[neighbor] and A[neighbor] == 0:  # 아직 방문하지 않은 실외 노드라면
            cnt += dfs(neighbor)  # DFS로 탐색 계속 진행
    return cnt  # 연결된 실내 노드 수 반환

answer = 0  # 정답을 저장할 변수 초기화

for i in range(n):  # 모든 노드에 대해 반복
    if A[i] == 1:  # 실내 노드라면
        for j in graph[i]:  # 인접한 노드들 중
            if A[j] == 1:  # 이웃도 실내라면
                answer += 1  # 실내 ↔ 실내 간선 1개 추가 (양쪽에서 세므로 나중에 나눌 예정)

for i in range(n):  # 모든 노드에 대해 반복
    if A[i] == 0 and not visited[i]:  # 실외 노드이고 아직 방문하지 않았다면
        cnt = dfs(i)  # 연결된 실내 노드 수를 DFS로 탐색
        answer += cnt * (cnt - 1)  # 조합 수(cntC2)를 계산하여 유효 경로 수에 더함

print(answer // 2)  # 실내-실내 간선을 중복 계산했기 때문에 2로 나눠서 출력
