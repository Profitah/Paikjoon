# 1년전 코드 gpt 리펙터링 Ver
from collections import deque

# 미로의 크기 입력받기
rows, cols = map(int, input().split())

# 미로 지도 입력받기 (2차원 리스트)
maze = []
for i in range(rows):
    line = input().strip()
    maze.append([int(c) for c in line])

# 이동할 수 있는 네 방향 (상, 하, 좌, 우)
move_row = [-1, 1, 0, 0]
move_col = [0, 0, -1, 1]

# BFS로 최단 거리 찾기
def bfs(start_row, start_col):
    # 큐를 생성하고 시작점을 넣음
    queue = deque()
    queue.append((start_row, start_col))

    # 큐가 빌 때까지 반복
    while queue:
        current_row, current_col = queue.popleft()

        # 네 방향으로 이동 시도
        for i in range(4):
            new_row = current_row + move_row[i]
            new_col = current_col + move_col[i]

            # 미로 바깥으로 나가면 무시
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue

            # 벽이면 무시
            if maze[new_row][new_col] == 0:
                continue

            # 처음 방문하는 길이면 (값이 1일 때만)
            if maze[new_row][new_col] == 1:
                # 이전 위치까지 거리 + 1 저장
                maze[new_row][new_col] = maze[current_row][current_col] + 1
                queue.append((new_row, new_col))

    # 도착지까지의 거리 반환
    return maze[rows - 1][cols - 1]

# 시작점 (0, 0)부터 탐색 시작
print(bfs(0, 0))