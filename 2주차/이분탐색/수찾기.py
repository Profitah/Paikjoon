n = int(input().strip())  # 탐색 대상의 개수 (리스트의 길이)
A = list(map(int, input().split()))  # 탐색 대상 리스트(A) 입력받기
A.sort()  # 이진 탐색을 수행하려면 반드시 정렬해야 함

m = int(input().strip())  # 찾아야 할 숫자의 개수
B = list(map(int, input().split()))  # 찾고자 하는 숫자 리스트 (B)

# 이진 탐색 함수 (Binary Search)
def binary_search(target_from_b, list_a): # 찾고자 하는 값과 탐색 대상 리스트
    current_min = 0  # 탐색 범위의 시작점 (왼쪽 포인터, pl)
    current_max = n - 1  # 탐색 범위의 끝점 (오른쪽 포인터, pr)
    cursor = (current_min + current_max) // 2  # 현재 탐색할 중앙값 (pc)

    # 탐색 범위가 유효한 동안 반복
    while current_min <= current_max:
        if list_a[cursor] == target_from_b:  # 현재 중앙값이 찾는 값과 일치하면
            return True  # 탐색 성공 (True 반환)

        elif list_a[cursor] < target_from_b:  # 현재 중앙값이 찾는 값보다 작다면
            current_min = cursor + 1  # 왼쪽 포인터 이동
        else:  # 현재 중앙값이 찾는 값보다 크다면
            current_max = cursor - 1  # 오른쪽 포인터 이동

        # 새로운 탐색 범위를 반영하여 중앙값(cursor) 업데이트
        cursor = (current_min + current_max) // 2

    return False  # 찾는 값이 없으면 False 반환

# B 리스트의 각 숫자에 대해 A 리스트에서 존재 여부 확인
for i in range(m):
    print(1 if binary_search(B[i], A) else 0)  # True면 1, False면 0 출력


""" 
참고자료 : 1. https://www.youtube.com/watch?v=wwqS53DPMw0 
             2. 자료구조와 함께 배우는 알고리즘 입문 (파이썬) 
"""