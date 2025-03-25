import sys
import heapq  # Python 내장 힙 모듈 (기본적으로 '최소힙(min-heap)'만 지원)

input = sys.stdin.readline
n = int(input())  # 명령의 개수 (총 입력 줄 수)

heap = []  # 힙(우선순위 큐)을 저장할 리스트. 기본은 최소힙이지만, 음수로 넣어 '최대힙'처럼 사용함

for _ in range(n):
    x = int(input())  # 정수 x 입력 받기

    if x == 0:
        # x가 0이면: 힙에서 가장 큰 값을 꺼내 출력해야 함
        if heap: #이건 **"heap이라는 리스트에 값이 있으면 True, 없으면 False"**로 평가됩니다.   | * 
            # Python의 heapq는 최소힙이므로, 최대값을 꺼내기 위해 -1을 곱해 저장했던 값을 다시 -1을 곱해 출력
            print(-heapq.heappop(heap))
        else:
            # 힙이 비어있으면 출력은 0
            print(0)
    else:
        # x가 자연수이면: 힙에 값을 추가 (최대힙을 구현하기 위해 음수로 저장)
        heapq.heappush(heap, -x)
        # 예: 5를 추가할 땐 -5를 push → heap은 [-5], 실제 의미는 [5]가 들어있는 셈
