x, y, w, h = map(int, input().split()) # 위치 입력 받기

"""
x = 한수의 현재 x좌표
y =  한수의 현재 y좌표
w =  직사각형의 오른쪽 끝 x 좌표
h =  직사각형의 위쪽 끝 y 좌표
"""

print(min(x, y, w-x, h-y)) # 최솟값 출력