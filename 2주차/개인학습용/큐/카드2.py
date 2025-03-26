from collections import deque

def my_card(N): # N장의 카드를 입력받아 실행되는 함수
    q = deque(range(1, N+1)) # 1부터 N이라는 값을 가지고 있는 수를 deque로 만들어 # deque는 양방향으로 데이터를 추가하거나 뺄 수 있는 queue

    while len(q) > 1: # queue의 길이가 1보다 크면
        q.popleft() # queue의 맨 앞에 있는 값을 제거하고
        q.append(q.popleft()) #새롭게 생긴 큐 맨 앞 값을 queue의 맨 뒤에 추가한다.
    return q[0] # 그리고 마지막에 남은 값을 반환한다.

N = int(input()) # N을 입력받고
print(my_card(N)) # my_card 함수 결과값을 출력하라.