# 최소힙에 음수를 추가하여 최대힙을 구현할 것임.
import heapq

def heap_sort(arr):
    heap = []
    
    # 배열의 모든 값을 최소 힙에 삽입
    for value in arr:
        heapq.heappush(heap, value)
    
    # 힙에서 하나씩 꺼내서 정렬된 리스트 생성
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    
    return sorted_arr

# 예시
data = [5, 3, 8, 1, 2, 7]
result = heap_sort(data)
print(result)  # 출력: [1, 2, 3, 5, 7, 8]
