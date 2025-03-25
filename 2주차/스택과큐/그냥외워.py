import sys
input = sys.stdint.readline

n = int(input()) # 명령어 수 입력
stack = []

for i in range (n):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])

        
    elif command[0] == 'pop':
        stack.pop() if stack else -1
        # stack.pop을 실행하고 stack이 비어있으면 -1을 출력한다.

    elif command[0] == 'size':
        stack.append(len(stack))
