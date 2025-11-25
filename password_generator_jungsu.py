# password_generator_jungsu.py

import random


def simple_password_generator(length=10):
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGITS = '0123456789'
    SYMBOLS = '!@#$%^&*'

    all_chars = LOWER + UPPER + DIGITS + SYMBOLS

    password_list = []

    for _ in range(length):
        random_char = random.choice(all_chars)
        password_list.append(random_char)

    random.shuffle(password_list)

    final_password = "".join(password_list)
    return final_password


def main():
    print("=== 랜덤 비밀번호 생성기 - 정수 ===")
    print("영문 대/소문자, 숫자, 특수문자를 포함한 랜덤 비밀번호를 생성합니다.\n")

    while True:
        raw = input("몇 자리 비밀번호를 생성할지 숫자로 입력 (q: 종료): ").strip()

        if raw.lower() == "q":
            print("프로그램을 종료합니다.")
            break

        try:
            length = int(raw)
        except ValueError:
            print("숫자만 입력하세요.\n")
            continue

        if length <= 0:
            print("0보다 큰 숫자를 입력하세요.\n")
            continue

        password = simple_password_generator(length)
        print(f"{length}자리 비밀번호: {password}\n")

        again = input("다시 생성할까요? (y/n): ").strip().lower()
        if again != "y":
            print("프로그램을 종료합니다.")
            break
        print()


if __name__ == "__main__":
    main()
