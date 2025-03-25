import sys

def is_valid_parentheses(string):
    stack = []
    
    for char in string:
        if char == '(':  # 여는 괄호는 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫는 괄호가 나오면 스택에서 '(' 제거
            if stack:
                stack.pop()
            else:
                return "NO"  # 스택이 비어있는데 ')'가 나왔으면 올바르지 않음
    
    return "YES" if not stack else "NO"  # 스택이 비어 있으면 올바른 괄호

# 여러 줄 입력 받기
n = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(n):
    line = sys.stdin.readline().strip()
    print(is_valid_parentheses(line))
