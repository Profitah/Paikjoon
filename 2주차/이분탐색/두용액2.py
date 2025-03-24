import sys
input = sys.stdin.readline 

N = int(input()) # 전체 용액의 수
N_list = list(map(int, input().split())) # 용액의 특성값 리스트
inf = float('inf') # 최소 절댓값 합을 양수로 저장
location = (0, 0) # 최적 쌍을 저장

for i in range(N - 1):  # 첫 번째 용액을 기준으로 선택 (마지막 전까지 N-1개만 선택) // 왜 N-1개인지 
    target = N_list[i] # 기준 용액. N_list의 i번째 값 
    high = N-1 # 
    while low <= high:
        mid = (low+high) // 2
        total = target + N_list[mid]
        
        if abs(total) < inf: 
            inf = abs(total)
            location = (N_list[i], N_list[mid])
        
        if total == 0:
            break
        elif total > 0:
            high = mid - 1
        else:
            low = mid + 1
    
print(*location)