import sys

def heapify(arr, n, i): # 배열, 배열의 길이, 노드 인덱스
    """ 반복문을 사용하여 힙 속성을 유지하는 함수 """
    while True: 
        largest = i  # 현재 노드를 가장 큰 값으로 가정
        left = 2 * i + 1  # 왼쪽 자식 노드 인덱스
        right = 2 * i + 2  # 오른쪽 자식 노드 인덱스

        # 왼쪽 자식이 존재하고, 현재 노드보다 크다면 largest 갱신
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # 오른쪽 자식이 존재하고, 현재 largest보다 크다면 largest 갱신
        if right < n and arr[right] > arr[largest]: 
            largest = right

        # largest가 변경되지 않았다면 힙 속성이 유지됨 -> 종료
        if largest == i:
            break

        # largest와 현재 노드(i)를 교환하여 힙 속성 유지
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # 갱신된 노드에서 다시 힙 속성 확인을 위해 이동
        i = largest

def heap_sort(arr):
    """ 반복문 기반의 힙 정렬 함수 """
    n = len(arr)  # 배열 크기

    # 최대 힙 구성 
    for i in range(n // 2 - 1, -1, -1):  # 내부 노드부터 루트까지 힙화
        heapify(arr, n, i) # 힙 구성

    #  힙에서 하나씩 요소를 꺼내 정렬 
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트(최댓값)를 끝으로 이동
        heapify(arr, i, 0)  # 남은 힙을 재정렬

N = int(sys.stdin.readline().strip())  # 첫 줄에서 정수 N을 입력받음

# N의 범위가 유효한지 검사 (1 <= N <= 1,000,000)
if not (1 <= N <= 1000000):
    print("1 <= N <= 1000000 범위의 정수만 입력해주세요")
else:
    # N개의 정수를 입력받아 리스트에 저장
    numbers = [int(sys.stdin.readline().strip()) for i in range(N)]

    # 입력된 수의 개수가 정확히 N개인지 확인
    if len(numbers) == N:
        heap_sort(numbers)  # 힙 정렬 실행

        # 정렬된 결과를 한 줄씩 출력
        for num in numbers:
            print(num)
    else: # 입력된 수의 개수가 N개가 아닌 경우
        print("입력 할 수 있는 숫자 조건을 확인해 주세요.")
