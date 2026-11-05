# 덧셈을 수행하는 함수
def add(a, b):
    return a + b

# 나눗셈을 수행하는 함수 (0으로 나누기 예외 처리 포함)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
