import sys
input = sys.stdin.readline

formula = input().rstrip()
minus = formula.split('-')
first = sum(map(int, minus[0].split('+')))
plus = []
for i in range(1, len(minus)):
    plus.append(sum(map(int, minus[i].split('+'))))
print(first - sum(plus))