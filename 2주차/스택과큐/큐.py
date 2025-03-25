import sys
input = sys.stdin.readline

import collections
n = int(input()) # 정수 n개를 입력받고 
queue = collections.deque() # deque를 사용하여 큐를 만든다. # 여기서 deque란, 양방향으로 데이터를 추가하거나 뺄 수 있는 queue이다.

for i in range(n): # n번 반복한다.
    command = input().split() # 명령어를 입력받는다.

    if command[0] == 'push': # 큐에 정수를 넣는다.
        queue.append(command[1]) # append() 함수를 사용하여 큐에 정수를 넣는다.

    elif command[0] == 'pop': # 큐에서 정수를 빼고, 빼낸 정수를 출력한다.
        if len(queue)==0: # 큐가 완전히 비어있을 때 
            print(-1) # -1을 출력한다.
        else:
            print(queue.popleft()) # popleft() 함수를 사용하여 큐에서 정수를 빼고, 빼낸 정수를 출력한다.
    elif command[0] == 'size': # 큐의 크기를 출력한다.
        print(len(queue)) # 큐의 길이를 출력한다.
    elif command[0] == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(queue)==0: # 만약에 큐가 완전히 비어있다면 
            print(1)
        else:
            print(0)
    elif command[0] == 'front': # 큐의 가장 앞에 있는 정수를 출력한다.
        if len(queue)==0: # 큐가 완전히 비어있을 때는
            print(-1) # -1을 출력한다.
        else:
            print(queue[0])
    else: 
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])