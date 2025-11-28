# simple_calculator_jincheol.py

def input_number(prompt: str) -> float:
    """숫자를 입력받아서 float으로 반환. 잘못 입력하면 다시 입력 요청."""
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("숫자를 올바르게 입력하세요.\n")


def calculate(num1: float, op: str, num2: float):
    """두 숫자와 연산자를 받아 계산 결과를 반환. 잘못된 연산자나 0 나누기 처리."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        return num1 / num2
    else:
        print("올바른 연산자를 입력하세요. (+, -, *, /)")
        return None


def main():
    print("=== 사칙연산 계산기 ===")
    print("두 숫자와 연산자를 입력하면 결과를 계산합니다.\n")

    while True:
        num1 = input_number("첫 번째 숫자를 입력하세요: ")

        op = input("연산자를 입력하세요 (+, -, *, /), 종료하려면 q: ").strip()
        if op.lower() == 'q':
            print("계산기를 종료합니다.")
            break

        num2 = input_number("두 번째 숫자를 입력하세요: ")

        result = calculate(num1, op, num2)
        if result is not None:
            print(f"결과: {result}\n")

        again = input("다시 계산하시겠습니까? (y/n): ").strip().lower()
        if again != 'y':
            print("계산기를 종료합니다.")
            break
        print()


if __name__ == "__main__":
    main()
