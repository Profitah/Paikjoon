from collections import deque  # BFS에 사용할 큐 자료구조 deque 불러오기

# 미로의 크기 입력받기 (행, 열)
rows, cols = map(int, input().split())

# 미로 지도 입력받기 (2차원 리스트 생성)
maze = []  # 전체 미로를 담을 리스트
for i in range(rows):
    line = input().strip()  # 한 줄 입력받기 (공백 없이)
    row = []  # 현재 줄의 각 숫자를 저장할 리스트
    for c in line:  # 입력받은 문자열의 문자 하나하나를 순회
        row.append(int(c))  # 문자를 정수로 변환해 row에 추가
    maze.append(row)  # 완성된 한 줄(row)을 미로에 추가

# 상하좌우 방향 벡터 (위, 아래, 왼쪽, 오른쪽)
move_row = [-1, 1, 0, 0]  # 행(row)의 이동 변화
move_col = [0, 0, -1, 1]  # 열(col)의 이동 변화

# BFS로 최단 거리 찾기
def bfs(start_row, start_col):
    queue = deque()  # 큐 생성
    queue.append((start_row, start_col))  # 시작 위치 삽입

    while queue:  # 큐가 빌 때까지 반복
        current_row, current_col = queue.popleft()  # 현재 위치 꺼내기

        for i in range(4):  # 상하좌우 4방향 확인
            new_row = current_row + move_row[i]  # 다음 이동할 행
            new_col = current_col + move_col[i]  # 다음 이동할 열

            # 미로 범위를 벗어나면 무시
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue

            # 벽(0)은 이동 불가
            if maze[new_row][new_col] == 0:
                continue

            # 처음 방문하는 길(1)이라면
            if maze[new_row][new_col] == 1:
                # 현재 위치까지의 거리 + 1 저장
                maze[new_row][new_col] = maze[current_row][current_col] + 1
                # 다음 탐색 대상으로 큐에 추가
                queue.append((new_row, new_col))

    # 도착 지점까지의 거리 반환
    return maze[rows - 1][cols - 1]

# 시작점 (0, 0)에서 BFS 실행 및 결과 출력
print(bfs(0, 0))