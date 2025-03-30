# 팀장님께서 강의해주신대로 크루스칼 알고리즘을 구현해보았습니다... 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 유니온 파인드 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 처리
V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 1. 간선 가중치 기준 정렬
edges.sort()

# 2. 유니온 파인드 초기화
parent = [i for i in range(V + 1)]

ans = 0
for cost, a, b in edges:
    # 3. 사이클이 생기지 않으면 선택
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += cost

print(ans)