import sys

input = sys.stdin.readline

# 사용자 입력값 처리
n, m = map(int, input().split())  # n: 나무의 수, m: 필요한 나무의 길이
tree_h = list(map(int, input().split()))  # 각 나무의 높이를 리스트로 입력받음

pl = 0  # 절단기 최소 높이 (left)
pr = max(tree_h)  # 절단기 최대 높이 (right) - 가장 높은 나무까지 자를 수 있음
result = 0  # 최적의 절단기 높이 결과 저장용

# 이진 탐색 시작
while pl <= pr:
    pc = (pl + pr) // 2  # 현재 중간값 (절단기 높이)
    total = sum(h - pc for h in tree_h if h > pc) 
    """"
    sum함수를 이용해 모두 더한다.
    무엇을? h - pc를
    어디서? tree_h에서
    언제? h가 pc보다 높을 때만
    """

# total = 0  # 자른 나무의 총 길이 계산용
# for i in range(n):
#     if tree_h[i] > pc:
#         total += tree_h[i] - pc  # pc보다 높은 나무만 잘려서 더해짐

    # 자른 나무 길이 총합이 필요한 길이 이상이면 절단기 높이를 올려도 됨
    if total >= m:
        pl = pc + 1
        result = pc  # 현재 높이로도 조건 만족하므로 결과 저장
    else:
        # 조건 만족 못하면 절단기 높이를 낮춤
        pr = pc - 1
# 최종 결과 출력
print(result)