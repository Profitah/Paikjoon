import sys  # sys 라이브러리 호출

def input():  # 사용자 입력 처리 함수 input
    return sys.stdin.readline()  # sys.stdin.readline()을 호출하여 입력을 처리

"""
sys.stdin.readline()은 내부적으로 더 낮은 메모리 사용을 위해 불필요한 가공 없이 원시 데이터를 처리합니다.
반면, input()은 더 많은 문자열 처리 및 메모리 할당이 필요하여 상대적으로 메모리를 더 많이 사용할 수 있습니다.
속도와 메모리 효율이 중요한 대규모 데이터 처리에서는 sys.stdin.readline()이 더 적합합니다.
"""

n = int(input())  # 사용자 입력으로 n 받아오기
count = [0] * 10001  # 0부터 10000까지의 숫자에 대한 카운트를 위한 리스트 초기화

for i in range(n):  # n번 동안 반복
    num = int(input())  # 정수를 입력받고
    count[num] += 1  # 수 정렬을 위해 해당 숫자의 인덱스 값을 1씩 증가시킨다.

# 1부터 10000까지 반복하면서 각 숫자의 출현 횟수만큼 출력
for i in range(1, 10001):  # 1부터 10000까지 반복
    if count[i] != 0:  # 해당 숫자가 등장한 적이 있다면
        for _ in range(count[i]):  # 해당 숫자가 등장한 횟수만큼 출력
            print(i)  # 숫자 출력