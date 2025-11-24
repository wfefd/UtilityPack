# string_tools_seunghwan.py

def to_upper(text: str) -> str:
    """문자열을 모두 대문자로 변환"""
    return text.upper()


# string_tools_seunghwan.py
# 문자열 처리 기능 구현 파일

def to_upper(s: str) -> str:
    """문자열을 대문자로 변환"""
    return s.upper()


def to_lower(s: str) -> str:
    """문자열을 소문자로 변환"""
    return s.lower()


def reverse_string(s: str) -> str:
    """문자열을 뒤집어서 반환"""
    return s[::-1]


def count_vowels(s: str) -> int:
    """문자열에서 모음(a,e,i,o,u) 개수 반환"""
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


def remove_spaces(s: str) -> str:
    """문자열의 모든 공백 제거"""
    return s.replace(" ", "")
# main.py
# 메뉴와 string_tools_seunghwan.py 기능 연동

import string_tools_seunghwan as st

# -*- coding: utf-8 -*-

def print_menu():
    print("\n===== 문자열 처리 프로그램 =====")
    print("1. 대문자로 변환")
    print("2. 소문자로 변환")
    print("3. 문자열 뒤집기")
    print("4. 문자열 모음 개수 세기")
    print("5. 공백 제거")
    print("0. 종료")
    print("===============================")

def main():
    while True:
        print_menu()
        
        choice = input("메뉴 선택: ")
        
        if choice == "0":
            print("프로그램 종료.")
            break
        
        s = input("문자열 입력: ")

        if choice == "1":
            print("결과:", st.to_upper(s))
        elif choice == "2":
            print("결과:", st.to_lower(s))
        elif choice == "3":
            print("결과:", st.reverse_string(s))
        elif choice == "4":
            print("모음 개수:", st.count_vowels(s))
        elif choice == "5":
            print("결과:", st.remove_spaces(s))
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
