valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:" # alphanumeric 문자를 등록한다.

T = int(input()) # 유저로부터 정수를 입력받는다. 

for i in range(T):  # 테스트 케이스 개수(T)만큼 반복
    R, S_input = input().split()  # 공백 기준으로 두 개의 값을 입력받음
    R = int(R)  # 첫 번째 값 R을 정수로 변환 (반복 횟수)

    # 입력받은 문자열(S_input)이 유효한 문자(영문자와 숫자)로만 구성되어 있는지 확인
    if all(char in valid_chars for char in S_input):   # if all : 모든 요소가 true인지 검증. (혹은 빈리스트인지 검증)
        # 문자열의 각 문자를 R번 반복하여 새로운 문자열을 생성
        result = ''.join(char * R for char in S_input)  
        print(result)  # 변환된 문자열 출력
    else:
        print('alphanumeric 문자만을 입력해주세요')  # 유효하지 않은 문자가 포함된 경우 오류 메시지 출력
