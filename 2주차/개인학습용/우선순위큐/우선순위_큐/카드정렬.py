import heapq # 힙 모듈 사용
import sys

input = sys.stdin.readline # 빠른입력 

n = int(input()) # 묶음의 개수 
heap = [] # 힙 생성 
for i in range(n): # 묶음의 개수만큼 반복
        heapq.heappush(heap, int(input())) # 힙에 묶음의 개수만큼 입력받은 값을 추가한다.

heapq.heapify(heap)  # 리스트를 우선순위 큐(최소 힙)으로 변환

total_cost = 0 # 총 비용

while len(heap) > 1: 
    # 가장 작은 두 묶음을 꺼낸다
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    cost = a + b  # 두 묶음을 합친 비용
    total_cost += cost  # total_cost + cost = 총 비용

    # 합친 묶음을 다시 큐에 넣는다
    heapq.heappush(heap, cost)

print(total_cost)

# python에서는 우선순위큐가 heapq이다.