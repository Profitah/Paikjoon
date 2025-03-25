import sys
input = sys.stdin.readline

import collections
n = int(input())
queue = collections.deque()

for i in range(n):
    command = input().split()

    if command[0] == 'push': # 큐에 정수를 넣는다.
        queue.append(command[1]) # append() 함수를 사용하여 큐에 정수를 넣는다.

    elif command[0] == 'pop': # 큐에서 정수를 빼고, 빼낸 정수를 출력한다.
        if len(queue)==0: # 큐가 완전히 비어있을 때 
            print(-1) # -1을 출력한다.
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else: 
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])