# 백준 2178

from collections import deque

rows, cols = map(int, input().split())

maze = []
for i in range(rows):
    line = input().strip() 
    row = []  
    for c in line: 
        row.append(int(c)) 
    maze.append(row) 
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