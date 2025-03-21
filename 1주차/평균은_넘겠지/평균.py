n = int(input())  # 테스트 케이스 개수를 입력받음

for i in range(n):  # 입력받은 테스트 케이스 개수(n)만큼 반복
    nums = list(map(int, input().split()))  # 한 줄의 숫자를 입력받아 공백 기준으로 분리 후 정수 리스트로 변환

    # nums[0]은 학생 수, nums[1:]은 점수 리스트
    avg = sum(nums[1:]) / nums[0]  # 점수들의 합을 학생 수로 나누어 평균 점수 계산

    # 평균을 초과하는 학생 수를 계산하여 전체 학생 수로 나눈 후 백분율 변환
    rate = (sum(score > avg for score in nums[1:]) / nums[0]) * 100  

    # 평균을 초과하는 학생 비율을 소수점 셋째 자리까지 출력
    print(f'{rate:.3f}%')
