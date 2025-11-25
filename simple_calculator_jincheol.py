print("사칙연산 계산기")

num1 = input("첫 번째 숫자를 입력하세요: ")
if not num1.isdigit():
    print("숫자를 올바르게 입력하세요.")
else:
    num1 = float(num1)
    op = input("연산자를 입력하세요 (+, -, *, /): ")
    num2 = input("두 번째 숫자를 입력하세요: ")
    
    if not num2.isdigit():
        print("숫자를 올바르게 입력하세요.")
    else:
        num2 = float(num2)
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
        else:
            print("올바른 연산자를 입력하세요.")
        
        if op in ['+', '-', '*', '/'] and not (op == '/' and num2 == 0):
            print("결과:", result)
