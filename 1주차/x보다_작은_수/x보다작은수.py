N,X = map(int, input().split()) # N X 입력받기

# 입력받은 숫자들을 리스트에 저장
A = list(map(int, input().split()))
    
# A의 각 숫자가 X보다 작으면 출력
for num in A:
     if num < X:
        print(num, end=' ')