import sys
input = sys.stdin.readline 

n = int(input())
stack = []                     
n = int(input())                 

for _ in range(n):            
    command = input().split()       

    if command[0] == 'push': 
        stack.append(int(command[1]))   
    elif command[0] == 'pop': 
        print(stack.pop() if stack else -1) # 삼항연산자
        # <참일 때 값> if <조건> else <거짓일 때 값>
        # 이 코드에서는 참일 때 stack.pop()을 출력하고, 거짓일 때 -1을 출력한다.

    elif command[0] == 'size': # 스택의 크기
        print(len(stack)) # 스택의 길이를 출력한다.


    elif command[0] == 'empty': 
        print(0 if stack else 1)


    else:  
        print(stack[-1] if stack else -1)
