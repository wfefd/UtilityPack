import random
import tkinter as tk
from tkinter import simpledialog, messagebox


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
    # Tkinter의 루트 윈도우 가져오기 (main_menu에서 이미 Tk() 만들어둔 상태)
    root = tk._default_root

    # 혹시 단독실행할 수도 있으니, root 없는 경우 방어 로직
    if root is None:
        # 그냥 콘솔 버전으로 동작
        try:
            length = int(input("몇 자리 비밀번호를 생성할 지 숫자 입력: "))
        except ValueError:
            print("숫자만 입력하세요.")
            return
        password = simple_password_generator(length)
        print(f"{length}자리 비밀번호: {password}")
        return

    # GUI 버전 입력창 (팝업)
    length = simpledialog.askinteger(
        "비밀번호 길이",
        "몇 자리 비밀번호를 생성할 지 숫자로 입력:",
        minvalue=4,
        maxvalue=64,
        parent=root
    )

    if length is None:
        # 취소 눌렀을 때
        return

    password = simple_password_generator(length)

    # 결과를 메시지 박스로 보여주기
    messagebox.showinfo(
        "랜덤 비밀번호",
        f"{length}자리 비밀번호:\n{password}"
    )


if __name__ == "__main__":
    main()
