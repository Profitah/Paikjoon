import sys

input = sys.stdin.readline
n,m = int(input().split()) # 베어낼 나무의 수와 상근이가 가져갈 나무의 길이
tree_h = list(map(int,(input().split()))) # 나무의 높이를 리스트 안에 담자

pl = 0 # 절단기의 최소 높이
pr = max(tree_h) # 절단기의 최대 높이
result = 0 # 최적의 절단기 높이 결과 저장용

while pl <= pr: # pl이 pr보다 작거나 같으면
    pc = (pl + pr) #  pl + pr // 2를 중간값(절단기의 현재 높이)로 설정하고

    total = sum(h - pc for h in tree_h if h > pc) # 나무 리스트에서 나무의 높이가 절단기의 높이보다 높은 것만 빼서 그것들의 합을 구한다.

    if total >= m: # 만약에 m이 total보다 작거나 같으면
        pl = pc + 1 # pl을 pc + 1로 설정하고
        result = pc # 현재 높이로도 조건을 만족하므로 결과를 저장한다.
    else: # 그게 아니라면
        pr = pc - 1 # pr을 pc - 1로 설정한다.
print(result) # 이후 결과를 출력한다.











