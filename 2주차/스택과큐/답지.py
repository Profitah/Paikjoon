import sys
input = sys.stdin.readline 

n = int(input()) # 실행시킬 명령어의 개수 입력
stack = [] # 스택 생성 #  스택을 만드는 방법에는 클래스를 이용하는 것과 리스트를 이용하는 것이 있는데, 여기서는 리스트를 이용하려고 한다.             

for i in range(n): #명령어의 개수 n만큼 반복   
     # i는 0부터 n-1까지의 인덱스로, 각 명령어의 순서를 나타낸다 (총 n개의 명령어 처리)
             
    command = input().split() # 명령어를 입력받는다.

    if command[0] == 'push': # 스택에 정수를 넣는다.
        stack.append(int(command[1])) # append() 함수를 사용하여 스택에 정수를 넣는다.
    elif command[0] == 'pop': # 스택에서 정수를 빼고, 빼낸 정수를 출력한다.
        print(stack.pop() if stack else -1) # 삼항연산자
        # <참일 때 값> if <조건> else <거짓일 때 값>
        # 이 코드에서는 참일 때 stack.pop()을 출력하고, 거짓일 때 -1을 출력한다.

    elif command[0] == 'size': # 스택의 크기
        print(len(stack)) # 스택의 길이를 출력한다.


    elif command[0] == 'empty': # 스택이 비어있으면, 1을 출력하고, 아니면 0을 출력한다.
        print(0 if stack else 1) # 삼항연산자
        # <참일 때 값> if <조건> else <거짓일 때 값>
        # 이 코드에서는 참일 때 0을 출력하고, 거짓일 때 1을 출력한다.


    else: # 위에서 제시된 모든 경우가 아니라면 
        print(stack[-1] if stack else -1) # 삼항연산자
        # <참일 때 값> if <조건> else <거짓일 때 값>
        # 이 코드에서는 참일 때 stack[-1]을 출력하고, 거짓일 때 -1을 출력한다.
        # stack[-1]은 현재 스택의 가장 위에 있는 정수를 의미한다.
        # 여기서 문제, 그렇다면 stack[0]은 무엇을 의미할까?
        # 답 : stack[0]은 현재 스택의 가장 아래에 있는 정수를 의미한다.
