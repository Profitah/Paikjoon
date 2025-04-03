expression = input().strip()

# 1. '-'를 기준으로 식을 나눕니다
parts = expression.split('-')

# 2. 첫 번째 그룹은 더합니다 (괄호 밖)
initial = sum(map(int, parts[0].split('+')))

# 3. 이후 그룹들은 모두 '+'로 나누어 합한 뒤, 빼줍니다
for part in parts[1:]:
    initial -= sum(map(int, part.split('+')))

print(initial)
