#(현재 인덱스 + K-1) % 남은 사람 수 
#N = 7, K = 3
#[1, 2, 3, 4, 5, 6, 7]
# delete_human = 0
#요세푸스 문제는 원형 큐처럼 작동하지만 rear 개념은 사용하지 않음. (데이터 삽입이 일어나지 않으므로)
# front만 이동시키면 됨.

"""
초기 상태:  [1, 2, 3, 4, 5, 6, 7]   (delete_human = 2)
3 제거 →   [1, 2, 4, 5, 6, 7]   (delete_human = 4)
6 제거 →   [1, 2, 4, 5, 7]   (delete_human = 1)
2 제거 →   [1, 4, 5, 7]   (delete_human = 3)
7 제거 →   [1, 4, 5]   (delete_human = 2)
5 제거 →   [1, 4]   (delete_human = 0)
1 제거 →   [4]   (delete_human = 0)
4 제거 →   []
"""

from collections import deque

N, K = map(int, input().split()) #사람 수 N, 제거할 사람 번호 K

queue = deque(range(1, N+1)) # 1부터 N까지의 수를 deque로 만듦 # deque는 양방향으로 데이터를 추가하거나 뺄 수 있는 queue #deque 사용 이유 : 한쪽에서 사람을 제거하는 것보다 양쪽에서 제거하는 것이 효율적이기 때문
result = [] # 제거된 사람들을 저장할 리스트

while queue: # queue가 빌 때까지 반복해라.
    queue.rotate(-(K-1))  # K-1번 왼쪽으로 회전 #rotate() 함수 :  deque의 요소들을 왼쪽으로 회전시키는 함수
    result.append(str(queue.popleft()))  # K번째 사람 제거

print("<" + ", ".join(result) + ">") # 지정된 형식으로 결과 출력