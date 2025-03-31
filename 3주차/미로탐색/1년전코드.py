from collections import deque

# 미로의 크기 입력받기
rows, cols = map(int, input().split())

# 미로 지도 입력받기 (2차원 리스트)
maze = []
for i in range(rows):
    line = input().strip() 
    row = []  # 한 줄씩 정수로 변환하여 리스트로 저장
    for c in line: # 라인에 입력 받은 각 문자열을 순회하며
        row.append(int(c)) # 각 문자를 정수로 변환하여 row 리스트에 추가한다.
    maze.append(row) #  # 완성된 한 줄을 maze에 추가

# 이동할 수 있는 네 방향 (상, 하, 좌, 우)
move_row = [-1, 1, 0, 0]
move_col = [0, 0, -1, 1]

# BFS로 최단 거리 찾기
def bfs(start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col))

    while queue:
        current_row, current_col = queue.popleft()

        for i in range(4):
            new_row = current_row + move_row[i]
            new_col = current_col + move_col[i]

            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue

            if maze[new_row][new_col] == 0:
                continue

            if maze[new_row][new_col] == 1:
                maze[new_row][new_col] = maze[current_row][current_col] + 1
                queue.append((new_row, new_col))

    return maze[rows - 1][cols - 1]

print(bfs(0, 0))