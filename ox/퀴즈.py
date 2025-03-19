testCaseCount = int(input())  # 테스트 케이스 개수를 정수로 입력받음

while testCaseCount:  # 남은 테스트 케이스 개수가 0보다 크면 반복
    inputString = input()  # OX 퀴즈 결과 문자열을 입력받음
             
    totalScore = 0  # 최종 점수를 저장할 변수 초기화
    consecutiveCount = 0  # 연속된 'O' 개수를 저장할 변수 초기화

    for char in inputString:  # 입력받은 문자열의 각 문자를 순차적으로 확인
        if char == 'O':  # 현재 문자가 'O'이면
            consecutiveCount += 1  # 연속된 'O' 개수를 증가
            totalScore += consecutiveCount  # 총 점수에 연속된 개수를 더함
        else:  # 현재 문자가 'X'이면
            consecutiveCount = 0  # 연속된 'O' 개수를 초기화 (연속 끊김)

    print(totalScore)  # 계산된 점수를 출력

    testCaseCount -= 1  # 남은 테스트 케이스 개수를 1 감소
