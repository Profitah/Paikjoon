try:
    N = int(input()) 
    수열A = list(map(int, input().split())) 
    plus, minus, multiply, divide = map(int, input().split())

    maximum_value = -int(1e9)
    minimum_value = int(1e9)

    def calculate(current_value, idx, plus, minus, multiply, divide):
        global maximum_value, minimum_value

        if idx == N:
            maximum_value = max(maximum_value, current_value)
            minimum_value = min(minimum_value, current_value)
            return

        next = 수열A[idx]

        if plus:
            calculate(current_value + next, idx + 1, plus - 1, minus, multiply, divide)
        if minus:
            calculate(current_value - next, idx + 1, plus, minus - 1, multiply, divide)
        if multiply:
            calculate(current_value * next, idx + 1, plus, minus, multiply - 1, divide)
        if divide:
            if current_value < 0:
                result = -(-current_value // next)
            else:
                result = current_value // next
            calculate(result, idx + 1, plus, minus, multiply, divide - 1)

    calculate(수열A[0], 1, plus, minus, multiply, divide)

    print(maximum_value)
    print(minimum_value)

except Exception as e:
    print("에러 발생:", e)
