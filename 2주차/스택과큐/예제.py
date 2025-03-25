from collections import deque

stack = deque()

# 1. push
stack.append(10)
stack.append(20)

# 2. top (스택 가장 위의 값)
print(stack[-1])  # 출력: 20

# 3. pop (스택에서 제거)
print(stack.pop())  # 출력: 20
print(stack.pop())  # 출력: 10

# 4. pop (더 이상 뺄 게 없음)
print(stack.pop() if stack else -1)  # 출력: -1

# 5. empty
print(0 if stack else 1)  # 출력: 1  → 비어있음

# 6. 다시 push
stack.append(30)

# 7. empty
print(0 if stack else 1)  # 출력: 0  → 비어있지 않음

# 8. top
print(stack[-1] if stack else -1)  # 출력: 30

#9 size
print(q.popleft() if q else -1)  # → -1 (비어있음)
q.append(100)


print(0 if q else 1)             # → 0 (비어있지 않음)