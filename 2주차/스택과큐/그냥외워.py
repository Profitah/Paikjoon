import sys
input = sys.stdint.readline

n = int(input()) # 명령어 수 입력
stack = []

for i in range (n):
    command = input().split()

    if command[0] == 'push':
        stack.append(command[1])

        
    elif command[0] == 'pop':
