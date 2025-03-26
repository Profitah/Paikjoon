import sys

input = sys.stdin.readline  # 입력 받기 위한 함수 (빠르게 입력을 받기 위해 사용)
n = int(input())  # 전체 종이의 한 변 크기 입력
paper_color = []  # 종이의 색을 저장할 리스트

# 종이 색 정보를 입력받아서 paper_color에 저장
for i in range(n):  # n 만큼 반복
    row = list(map(int, input().split()))  # 한 줄씩 입력받아서 공백 기준으로 나누고 정수로 변환
    paper_color.append(row)  # 각 줄의 색 정보를 종이 색 리스트에 추가

# 색을 True/False로 설정 (True는 파란색, False는 흰색)
blue = True  # 파란색은 True로 설정
white = False  # 흰색은 False로 설정

# 종이 영역이 모두 같은 색인지 확인하는 함수
def is_same_color(x, y, size, color):
    for row_iterator in range(x, x + size):  # x부터 x + size까지, 즉 시작 좌표부터 영역 크기까지 반복
        for column_iterator in range(y, y + size):  # y부터 y + size까지 반복, 영역의 세로 길이를 순차적으로 확인
            if paper_color[row_iterator][column_iterator] != color:  # 현재 위치의 색이 원하는 색과 다르면
                return "다른색 있음"  # 행이나 열에 다른 색의 종이가 있다면 "다른 색"을 반환
    return "같은 색"  # 모든 행과 열이 같은 색이라면 "같은 색" 반환

# 종이를 4등분하여 색을 확인하는 함수
def check(x, y, size):
    true_count = 0  # True (파란색)의 개수를 세는 변수
    false_count = 0  # False (흰색)의 개수를 세는 변수
    color = paper_color[x][y]  # 첫 번째 칸의 색을 기준으로 확인 (이 색을 기준으로 영역이 같은지 확인)

    # 해당 영역이 모두 같은 색인지 확인
    color_status = is_same_color(x, y, size, color)  # is_same_color 함수 호출로 해당 영역이 모두 같은 색인지 확인
    
    if color_status == "같은 색":  # 영역이 같은 색이라면
        if color == 1:  # 파란색이면 (color가 1이면 파란색)
            true_count += 1  # True (파란색) 색종이 개수 증가
        else:  # 흰색이면 (color가 0이면 흰색)
            false_count += 1  # False (흰색) 색종이 개수 증가
    else:  # 영역이 다른 색이라면
        new_size = size // 2  # 4등분하기 위해 크기를 반으로 나눔
        # 영역을 4등분하여 재귀적으로 색을 확인
        t1, f1 = check(x, y, new_size)  # 좌상단 영역
        t2, f2 = check(x, y + new_size, new_size)  # 우상단 영역
        t3, f3 = check(x + new_size, y, new_size)  # 좌하단 영역
        t4, f4 = check(x + new_size, y + new_size, new_size)  # 우하단 영역
        
        # 4등분된 영역들에서 나온 결과를 합산
        true_count = t1 + t2 + t3 + t4  # True (파란색) 색종이 개수 합산
        false_count = f1 + f2 + f3 + f4  # False (흰색) 색종이 개수 합산
    
    return true_count, false_count  # 최종적으로 True (파란색)과 False (흰색) 색종이의 개수를 반환

# 첫 번째 호출 (전체 영역을 확인)
true_count, false_count = check(0, 0, n)  # (0, 0)에서부터 크기 n의 종이 영역을 확인

# 결과 출력
print(false_count)  # 흰색 색종이의 개수를 출력
print(true_count)   # 파란색 색종이의 개수를 출력
