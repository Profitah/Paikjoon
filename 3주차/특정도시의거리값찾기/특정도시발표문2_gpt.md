## 📌 문제 개요

이 발표에서는 BFS(너비 우선 탐색)를 활용하여 출발 도시로부터 특정 거리(K)에 위치한 도시를 찾는 알고리즘을 설명합니다.  
다음은 예시 입력입니다:

```
도시 수: N = 4  
도로 수: M = 4  
목표 거리: K = 2  
출발 도시: X = 1  

도로 정보:
1 → 2  
1 → 3  
2 → 3  
2 → 4
```

```python
n, m, k, x = map(int, input().split())  # 도시 수n, 도로 수m, 목표 거리 k, 출발 도시 x
```

---

## 📐 도로망 구조

도시와 도로를 그래프로 표현하면 다음과 같습니다:

```
[1] → [2] → [4]
 ↓     ↓
 → [3] ←
```

- 1번 도시에서 2번과 3번으로 이동 가능  
- 2번 도시에서 3번과 4번으로 이동 가능

### 왜 인접 리스트를 사용할까?
이 문제에서는 도시 간의 연결 관계를 표현하기 위해 **인접 리스트**를 사용합니다.  
- **상황**: 도로가 단방향이고, 각 도시에서 연결된 도시의 수가 적을 때(희소 그래프).  
- **이유**: 인접 행렬은 N×N 크기의 2차원 배열을 필요로 하지만, 인접 리스트는 실제 연결된 도로만 저장하므로 메모리를 효율적으로 사용하며, 연결된 도시를 빠르게 탐색할 수 있습니다.

```python
# 인접 리스트 생성
graph = []
for i in range(n + 1):
    graph.append([])  # 각 도시마다 연결된 도시를 저장할 리스트 추가

# 간선 정보 입력 → 인접 리스트에 저장
for j in range(m):
    a, b = map(int, input().split())  # a번 도시에서 b번 도시로 이동 가능 (단방향)
    graph[a].append(b)
```

---

## 📦 초기 설정

알고리즘을 시작하기 위해 **거리 리스트**를 초기화합니다.  
- 출발 도시(1번)는 거리 0, 나머지는 방문 전이므로 -1로 설정합니다.

| 도시 번호 | 거리 리스트 (`road_distance`) |
|-----------|-------------------------------|
| 0         | -1 (사용 안 함)              |
| 1         | 0 (출발 도시)                |
| 2         | -1 (미방문)                  |
| 3         | -1 (미방문)                  |
| 4         | -1 (미방문)                  |

- **큐**를 사용하여 탐색 순서를 관리하며, 처음에는 `[1]`로 시작합니다.

### 왜 거리 리스트와 큐를 사용할까?
- **거리 리스트**:
  - **상황**: 각 도시까지의 최단 거리를 기록해야 할 때.  
  - **이유**: 배열을 사용하면 각 도시의 거리를 O(1) 시간에 확인하고 갱신할 수 있어, BFS의 최단 경로 계산에 적합합니다.  
- **큐**:
  - **상황**: 도시를 거리순으로 탐색해야 할 때(선입선출, FIFO).  
  - **이유**: BFS는 가까운 도시부터 차례대로 방문해야 하며, 큐는 먼저 들어온 도시를 먼저 처리함으로써 이 순서를 보장합니다.

```python
# 거리 정보를 저장할 리스트 (-1: 방문하지 않음)
road_distance = [-1] * (n + 1)

# BFS 함수 정의
def bfs(start):
    q = deque([start])  # 시작 도시를 큐에 삽입
    road_distance[start] = 0  # 시작 도시의 거리는 0
```

---

## 🧭 BFS 탐색 과정

BFS는 출발점에서 가까운 도시부터 순차적으로 탐색하는 방식입니다.  
각 단계를 자세히 살펴보겠습니다.

```python
# BFS 함수 내부
def bfs(start):
    q = deque([start])
    road_distance[start] = 0
    while q:
        current = q.popleft()  # 큐에서 현재 도시 꺼내기
        for next_city in graph[current]:  # 연결된 도시들 탐색
            if road_distance[next_city] == -1:  # 방문하지 않은 도시라면
                road_distance[next_city] = road_distance[current] + 1  # 거리 갱신
                q.append(next_city)  # 다음 도시를 큐에 삽입
```

---

### 1단계: 1번 도시 탐색
- 연결된 도시: 2번, 3번  
- 미방문 도시이므로 거리를 0 + 1 = 1로 갱신

| 도시 번호 | 거리 리스트 |
|-----------|-------------|
| 0         | -1          |
| 1         | 0           |
| 2         | 1           |
| 3         | 1           |
| 4         | -1          |

- 큐: `[2, 3]`

---

### 2단계: 2번 도시 탐색
- 연결된 도시: 3번, 4번  
- 3번은 이미 방문됨 (거리 1 유지)  
- 4번은 미방문, 거리 1 + 1 = 2로 갱신

| 도시 번호 | 거리 리스트 |
|-----------|-------------|
| 0         | -1          |
| 1         | 0           |
| 2         | 1           |
| 3         | 1           |
| 4         | 2           |

- 큐: `[3, 4]`

---

### 3단계: 3번 도시 탐색
- 연결된 도시: 없음  
- 추가 작업 없이 진행

| 도시 번호 | 거리 리스트 |
|-----------|-------------|
| 0         | -1          |
| 1         | 0           |
| 2         | 1           |
| 3         | 1           |
| 4         | 2           |

- 큐: `[4]`

---

### 4단계: 4번 도시 탐색
- 연결된 도시: 없음  
- 큐가 비며 탐색 종료

| 도시 번호 | 거리 리스트 |
|-----------|-------------|
| 0         | -1          |
| 1         | 0           |
| 2         | 1           |
| 3         | 1           |
| 4         | 2           |

- 큐: `[]`

```python
# BFS 실행
bfs(x)
```

---

## ✅ 탐색 결과

최종 거리 리스트를 확인하면:

| 도시 번호 | 거리 |
|-----------|------|
| 1         | 0    |
| 2         | 1    |
| 3         | 1    |
| 4         | 2    |

---

## 🎯 목표 거리(K=2) 도시 출력

- 목표 거리 K=2에 해당하는 도시: **4번 도시**  
- 결과 출력:

```
4
```

- 만약 해당 거리의 도시가 없다면 "-1"을 출력합니다.

```python
# 거리 K인 도시를 찾고 출력
found = False  # 조건에 맞는 도시가 있는지 여부
for i in range(1, n + 1):
    if road_distance[i] == k:
        print(i)
        found = True

# 조건에 맞는 도시가 하나도 없다면 -1 출력
if not found:
    print(-1)
```

---

## 🧠 알고리즘 핵심 요약

| 요소            | 설명                              |
|-----------------|-----------------------------------|
| BFS            | 가까운 도시부터 순차적으로 탐색    |
| 거리 리스트    | 각 도시까지의 최단 거리 기록      |
| 큐             | 탐색 순서를 관리                  |
| 방문 체크      | 중복 방문을 방지하여 최단 거리 보장 |
| 출력 조건      | 거리 K인 도시를 오름차순으로 출력 |

---

## ✅ 결론

BFS 알고리즘은 출발 도시에서 시작하여 도로를 따라 한 단계씩 거리를 계산하며,  
최종적으로 목표 거리 K에 해당하는 도시를 효율적으로 찾아냅니다.  
이 방식은 시간 복잡도 O(N + M)으로, 도시 수(N)와 도로 수(M)에 비례하여 동작합니다.  
인접 리스트, 큐, 거리 리스트를 사용함으로써 메모리와 시간을 최적화하며,  
실제 경로 탐색 문제(예: 내비게이션 시스템, 네트워크 분석)에도 유용하게 적용될 수 있습니다.

```python
import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
road_distance = [-1] * (n + 1)
graph = [[] for _ in range(n + 1)]

for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    road_distance[start] = 0
    while q:
        current = q.popleft()
        for next_city in graph[current]:
            if road_distance[next_city] == -1:
                road_distance[next_city] = road_distance[current] + 1
                q.append(next_city)

bfs(x)

found = False
for i in range(1, n + 1):
    if road_distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
```