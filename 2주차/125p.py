from typing import Any, Sequence  # 타입 힌트를 위한 모듈 (리스트나 임의 타입 지원)

def bin_search(a: Sequence, key: Any) -> int:  # 이진 탐색 함수: 정렬된 a에서 key 값을 찾아 그 인덱스를 반환
    pl = 0                      # 왼쪽 포인터: 탐색 범위의 시작 인덱스
    pr = len(a) - 1            # 오른쪽 포인터: 탐색 범위의 끝 인덱스

    while True:                # 무한 반복 시작 (찾거나 범위가 없어질 때까지)
        pc = (pl + pr) // 2    # 가운데 인덱스를 계산 (중간 값의 위치)
        
        if a[pc] == key:       # 가운데 값이 찾는 값이면
            return pc          # 그 인덱스를 바로 반환

        elif a[pc] < key:      # 가운데 값보다 찾는 값이 크면
            pl = pc + 1        # 왼쪽 범위를 중간 오른쪽으로 이동

        else:                  # 가운데 값보다 찾는 값이 작으면
            pr = pc - 1        # 오른쪽 범위를 중간 왼쪽으로 이동

        if pl > pr:            # 포인터가 역전되면 (탐색 범위가 사라지면)
            break              # 반복 종료

    return -1                  # 값을 찾지 못한 경우 -1 반환

if __name__ == '__main__':     # 직접 실행할 때만 아래 코드 실행 (import시에는 실행 안 됨)
    num = int(input('원소 수를 입력하세요.: '))  # 사용자로부터 원소 개수 입력 받음
    x = [None] * num                       # 입력 받은 개수만큼 빈 리스트 생성

    print('배열 데이터를 오름차순으로 입력하세요.')  # 사용자에게 오름차순으로 입력하라고 안내

    x[0] = int(input('x[0]: '))           # 첫 번째 값은 바로 입력
    for i in range(1, num):               # 두 번째 원소부터 입력 받기
        while True:                       # 오름차순 보장 위한 반복
            x[i] = int(input(f'x[{i}]: '))  # i번째 원소 입력
            if x[i] >= x[i - 1]:            # 바로 앞 원소보다 크거나 같으면 OK
                break                       # 탈출


    ky = int(input('검색할 값을 입력하세요.: '))  # 찾고자 하는 값을 입력 받음

    idx = bin_search(x, ky)                      # 이진 탐색 함수 호출 → 결과 인덱스를 받음

    if idx == -1:                                # 결과가 -1이면 (못 찾음)
        print('검색값을 갖는 원소가 존재하지 않습니다.')  # 존재하지 않는다고 출력
    else:                                        # 찾은 경우
        print(f'검색값은 x[{idx}]에 있습니다.')         # 인덱스와 함께 출력