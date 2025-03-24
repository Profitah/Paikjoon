a = int(input()) # 명령의 수 N을 입력받는다.

stack = [] # 스택을 만든다.

명령 = [input().split() for i in range(a)] 

def push(x):
    stack.append(int(i[1]))

def pop(x):
    stack.append(int(i[1]))

def size(x):
    stack.append(int(i[1]))

def top(x):
    stack.append(int(i[1]))

def empty(x):    
    if stack:
        print(1)
    else:
        print(0)

for i in 명령:
    if i[0] == 'push':
        push(i[1])
    elif i[0] == 'pop':
        pop(i[1])
    elif i[0] == 'size':
        size(i[1])
    elif i[0] == 'empty':
        empty(i[1])
    elif i[0] == 'top':
        top(i[1])
    else:
        continue