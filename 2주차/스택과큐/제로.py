import sys
from collections import deque # 양방향으로 데이터를 추가하거나 뺄 수 있는 queue


K = int(input()) # 주어지는 줄 수 
record = [] # 입력값을 저장할 리스트 
zero_count = deque() # deque 선언

for i in range(K): # k번 반복 (사용자가 입력한 수)
    record.append(int(input())) # 사용자 입력값을 record 리스트에 추가

for i in range(K): # k번 반복 (사용자가 입력한 수)
    if record[i] == 0: # 사용자 입력값이 0이면
        zero_count.pop() # q에서 가장 오른쪽에 있는 값을 삭제
    else:  # 사용자 입력값이 0이 아닌 다른 수라면,
        zero_count.append(record[i]) # q에 사용자가 입력한 값 record[i]를 추가

print(sum(zero_count)) # q에 있는 모든 값을 더한 값을 출력
