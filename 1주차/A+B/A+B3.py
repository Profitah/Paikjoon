T = int(input()) # 사용자에게 테스트 케이스의 개수 정수로  입력받기

for i in range(1, T+1): # T만큼 반복하여
    A, B = map(int, input().split()) # A, B 입력받기
    print(A + B) # A + B 더하여 출력하기
