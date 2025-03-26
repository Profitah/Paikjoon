import sys
input = sys.stdin.readline

# 입력처리
N = int(input()) # 탑들의 개수
N2 = list(map(int, input().split())) # 탑들의 높이를 입력받는다
stack = [] # 스택 생성
solution = [0] * N # 스택을 0으로 초기화하고, 입력받을 개수만큼 크기 늘리기. | 이게 필요한 이유 : 스택에 들어가있는 값이 몇번째 탑인지도 코드 실행에 필요 하기 때문이다.

for i in range(N): # 사용자에게 입력받은 만큼 반복한다.
    while stack: # 스택이 비어있지 않은한, 
        if stack[-1][1] > N2[i]: # 스택의 마지막값과 입력받은 값을 비교한다.  스택의 마지막 값이 더 크면
            solution[i] = stack[-1][0] + 1 # 스택의 마지막 값의 인덱스에 1 더한 값을 solution에 넣는다.
            break # 반복문을 탈출한다.
        else: # 그 외의 경우 
            stack.pop() # 스택의 끝에서 값을 제거한다.
    stack.append((i, N2[i])) # 스택에 인덱스값과 입력받은 값을 추가한다.
print(*solution) # solution 스택을 언패킹하여 출력한다.