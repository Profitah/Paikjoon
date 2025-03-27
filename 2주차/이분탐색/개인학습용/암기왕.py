import sys
input = sys.stdin.readline

T = int(input())  

for i in range(T):
    N = int(input())
    수첩1 = list(map(int, input().split()))
    수첩1.sort()  

    M = int(input())
    수첩2 = list(map(int, input().split()))

    for 오늘의_정수 in 수첩2:
        pl = 0
        pr = N - 1
        탐색 = False

        while pl <= pr:
            pc = (pl + pr) // 2
            if 수첩1[pc] == 오늘의_정수:
                탐색 = True
                break
            elif 수첩1[pc] < 오늘의_정수:
                pl = pc + 1
            else:
                pr = pc - 1
        if 탐색:
            print(1)
        else:
            print(0)

    """
    import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = set(map(int, input().split()))  # set 사용

    M = int(input())
    note2 = list(map(int, input().split()))

    print('\n'.join(['1' if x in note1 else '0' for x in note2]))

    
    """

