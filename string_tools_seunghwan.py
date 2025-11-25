def convert_uppercase(text):
    return text.upper()

def convert_lowercase(text):
    return text.lower()

def reverse_text(text):
    return text[::-1]

def count_text_length(text):
    return len(text)

def main():
    while True:
        print("===== 문자열 처리 프로그램 =====")
        print("1. 대문자로 변환")
        print("2. 소문자로 변환")
        print("3. 글자 뒤집기")
        print("4. 글자 수 세기")
        print("5. 문자열 입력하기")
        print("0. 종료")
        print("===============================")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            print("결과:", convert_uppercase(user_text))

        elif choice == "2":
            print("결과:", convert_lowercase(user_text))

        elif choice == "3":
            print("결과:", reverse_text(user_text))

        elif choice == "4":
            print("글자 수:", count_text_length(user_text))

        elif choice == "5":
            global user_text
            user_text = input("새 문자열 입력: ")

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")

        print()

# 전역변수 초기값
user_text = ""

if __name__ == "__main__":
    main()
