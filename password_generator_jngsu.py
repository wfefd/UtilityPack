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

len = int(input("몇 자리 비밀번호를 생성할 지 숫자 입력: "))
password = simple_password_generator(len)
print(f"{len}자리 비밀번호: {password}")
