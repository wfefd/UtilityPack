# main_menu.py
# 터미널 버전 메인 메뉴

# 각 기능 파일 import (없으면 None으로 둔다)
try:
    import unit_converter_hyungkyu as mod_unit
except ImportError:
    mod_unit = None

try:
    import simple_calculator_jincheol as mod_calc
except ImportError:
    mod_calc = None

try:
    import score_average_harin as mod_score
except ImportError:
    mod_score = None

try:
    import string_tools_seunghwan as mod_string
except ImportError:
    mod_string = None

# 파일 이름이 password_generator_jungsu.py 라고 가정
try:
    import password_generator_jngsu as mod_pw
except ImportError:
    mod_pw = None


def run_module(mod, label: str):
    """모듈과 label을 받아서 main()을 실행하거나, 없으면 안내 메시지."""
    if mod is None:
        print(f"[안내] {label} 기능 파일이 아직 존재하지 않습니다.")
        print("       담당자가 파일을 생성하고 커밋해야 합니다.\n")
        return

    if not hasattr(mod, "main"):
        print(f"[오류] {label} 모듈에 main() 함수가 없습니다.")
        print("       파일 안에 def main(): 을 만들어 주세요.\n")
        return

    # 실제 기능 실행
    print(f"\n>>> {label} 실행\n")
    mod.main()
    print(f"\n>>> {label} 종료\n")


def open_unit_converter():
    run_module(mod_unit, "단위 변환기 (형규)")


def open_simple_calculator():
    run_module(mod_calc, "간단 계산기 (진철)")


def open_score_average():
    run_module(mod_score, "점수 평균 계산 (하린)")


def open_string_tools():
    run_module(mod_string, "문자열 처리 (승환)")


def open_password_generator():
    run_module(mod_pw, "랜덤 비밀번호 생성기 (정수)")


def create_main_menu():
    """터미널용 메인 메뉴 루프"""
    while True:
        print("===================================")
        print("         Team Utility Pack         ")
        print("===================================")
        print("1. 단위 변환기 (형규)")
        print("2. 간단 계산기 (진철)")
        print("3. 점수 평균 계산 (하린)")
        print("4. 문자열 처리 (승환)")
        print("5. 랜덤 비밀번호 생성기 (정수)")
        print("0. 종료")
        print("===================================")

        choice = input("사용할 기능 번호를 선택하세요: ").strip()
        print()

        if choice == "1":
            open_unit_converter()
        elif choice == "2":
            open_simple_calculator()
        elif choice == "3":
            open_score_average()
        elif choice == "4":
            open_string_tools()
        elif choice == "5":
            open_password_generator()
        elif choice == "0" or choice.lower() == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 0~5 사이의 번호를 입력하세요.\n")


if __name__ == "__main__":
    create_main_menu()
