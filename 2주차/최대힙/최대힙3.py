import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 최소힙으로 최대힙을 구현하고 있기 때문에 음수로 저장했던 값을 다시 음수로 출력

    else:
        heapq.heappush(heap, -x) # 최소힙으로 최대힙을 구현하고 있기 때문에 음수로 저장