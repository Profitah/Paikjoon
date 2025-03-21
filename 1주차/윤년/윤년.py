year = int(input()) # 년도 

 # 중첩 if문
if (year % 4 == 0): # 4의 배수이고
        if  (year % 100 !=0 or year % 400 == 0) : # 100의 배수가 아니거나 400의 배수인 경우 판별
            print(1) # 모든 조건을 통과했다면 1 출력
        else :
            print(0)

else : # if-else 문 사용
    print(0) # 윤년이 아닌 경우에는 0 출력