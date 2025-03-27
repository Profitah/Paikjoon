"""import sys

input = sys.stdin.readline
stack = []

N = int(input())  # 입력 개수

# N만큼 입력받기
for J in range(N):
    stack.append(input()[::-1])

# 스택에서 하나씩 꺼내어 역순으로 출력
for Z in range(N):
    print(stack.pop(), end="")

# 단어 순서를 바꾸지 않는 것이 정답 조건이라고 함."
"""

import sys

input = sys.stdin.readline

N = int(input())  
result = []      

for j in range(N):
    user_input = input().strip()
    stack = []
    keyword = ''

    for char in user_input:
        if char == ' ':
            while stack:
                keyword += stack.pop()
            keyword += ' '
        else:
            stack.append(char)

    while stack:
        keyword += stack.pop()

    result.append(keyword)

print('\n'.join(result))

#  주석 귀찮...