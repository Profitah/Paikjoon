import sys
input = sys.stdin.readline

# 입력처리
N = int(input())  # 탑들의 개수
N2 = list(map(int, input().split()))  # 탑들의 높이를 입력받는다
stack = []  # 스택 생성
solution = [0] * N  # 스택을 0으로 초기화하고, 입력받을 개수만큼 크기 늘리기
tower_h = N2[::-1]  # N2를 뒤집어서 저장한다

for i in range(N):  # 사용자에게 입력받은 만큼 반복한다
    # 현재 탑보다 높은 탑이 있을 때까지 스택에서 꺼낸다
    while stack and tower_h[i] >= stack[-1][0]:  # stack[-1][0]은 탑의 높이
        stack.pop()
    
    if stack:
        solution[i] = stack[-1][1]  # stack[-1][1]은 탑의 번호
    
    stack.append((tower_h[i], i + 1))  # (탑의 높이, 탑의 번호) 쌍을 스택에 저장

# 출력
print(*solution)  # solution 배열을 공백을 두고 출력
