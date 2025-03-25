import sys
input = sys.stdin.readline

import collections
n = int(input()) # 정수 n개를 입력받고 
queue = collections.deque() # deque를 사용하여 큐를 만든다. # 여기서 deque란, 양방향으로 데이터를 추가하거나 뺄 수 있는 queue이다.
# deque는 "양방향 가능"이지, "양방향 필수"는 아니다.

for i in range(n): # n번 반복한다.
     # i는 0부터 n-1까지의 인덱스로, 각 명령어의 순서를 나타낸다 (총 n개의 명령어 처리)
     
    command = input().split() # 명령어를 입력받는다.

    if command[0] == 'push': # 큐에 정수를 넣는다.
        queue.append(command[1]) # append() 함수를 사용하여 큐에 정수를 넣는다.

    elif command[0] == 'pop': # 큐에서 정수를 빼고, 빼낸 정수를 출력한다.
        if len(queue)==0: # 큐가 완전히 비어있을 때 
            print(-1) # -1을 출력한다.
        else:
            print(queue.popleft()) # popleft() 함수를 사용하여 큐에서 정수를 빼고, 빼낸 정수를 출력한다. # 정수는 앞에서 부터 출력한다. popleft()  
    elif command[0] == 'size': # 큐의 크기를 출력한다.
        print(len(queue)) # 큐의 길이를 출력한다.
    elif command[0] == 'empty': # 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(queue)==0: # 만약에 큐가 완전히 비어있다면 
            print(1) # 1을 출력하라 
        else: # 그게 아니면 
            print(0) # 0을 출력하라
    elif command[0] == 'front': # command 리스트의 첫 번째 요소가 "front"일 때 
        if len(queue)==0: # 큐가 완전히 비어있을 때는
            print(-1) # -1을 출력한다.
        else: # 그게 아니면 
            print(queue[0]) # 큐의 첫 번째 요소를 출력한다.
    else: # 그게 아니면 
        if len(queue)==0: # 큐가 완전히 비어있을 때 
            print(-1) # -1을 출력한다.
        else: # 그게 아니면 
            print(queue[-1]) # 큐의 마지막 요소를 출력 한다.