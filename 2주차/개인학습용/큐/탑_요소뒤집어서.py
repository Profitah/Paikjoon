import sys

input = sys.stdin.readline # 빠른 입력
N = int(input())  # 탑의 개수 N
TowerHeights = list(map(int, input().split()))  # 탑들의 높이를 입력받는다
stack = []  # 스택 생성
solution = [0] * N  # 스택을 0으로 초기화하고, 입력받을 개수만큼 크기 늘리기

for i in range(N):  # 사용자에게 입력받은 만큼 반복한다.
    # 현재 탑보다 높은 탑이 있을 때까지 스택에서 꺼낸다
    while stack and TowerHeights[i] >= TowerHeights[stack[-1]]:  # stack[-1]은 현재 스택의 인덱스 stack[i]는 현재 탑의 높이
        stack.pop()  # 현재 탑보다 작은 탑을 배열에서 제거
    
    if stack:
        solution[i] = stack[-1] + 1  # 스택에 있는 마지막 탑의 번호를 solution에 저장 
    
    stack.append(i)  # 현재 탑의 인덱스를 스택에 추가

# 결과 출력
print(*solution)  # solution 배열을 공백을 두고 출력