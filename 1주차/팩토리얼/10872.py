"""
팩토리얼을 만드는 방법에는 재귀함수를 이용하는 방법과 반복문을 이용하는 방법,
총 2가지 방법이 있다.
"""

# 1. 반복문을 이용한 방법
N = int(input())  # N을 입력받음
factorial = 1  # 팩토리얼을 저장할 변수

for i in range(1, N + 1):  # 1부터 N까지 반복
    factorial *= i  # 팩토리얼 계산

print(f"{factorial}")  # 결과 출력


# 2. 재귀함수를 이용한 방법
def factorial_recursive(n):
    # 종료 조건: n이 1 이하일 때, 팩토리얼 값 1 반환
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)  # n * factorial(n-1)

N = int(input())  # N을 입력받음
result = factorial_recursive(N)  # 재귀 함수 호출

print(f"{result}")  # 결과 출력
