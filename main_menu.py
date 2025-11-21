# main_menu.py
import tkinter as tk
from tkinter import messagebox

# 각 기능 파일 import (없으면 None으로 둔다)
try:
    import unit_converter_hyungkyu as mod_unit
except ImportErroru:
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

try:
    import password_generator_jungsu as mod_pw
except ImportError:
    mod_pw = None


def run_module(mod, label: str):
    """모듈과 label을 받아서 main()을 실행하거나, 없으면 안내 메시지."""
    if mod is None:
        messagebox.showinfo("준비 중", f"{label} 기능 파일이 아직 존재하지 않습니다.\n"
                                      f"해당 담당자가 파일을 커밋해야 합니다.")
        return

    if not hasattr(mod, "main"):
        messagebox.showinfo("오류", f"{label} 모듈에 main() 함수가 없습니다.\n"
                                   f"파일 안에 def main(): 을 만들어 주세요.")
        return

    # 실제 기능 실행
    mod.main()


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


def create_main_window():
    root = tk.Tk()
    root.title("Team Utility Pack")
    root.geometry("420x320")

    title_label = tk.Label(
        root,
        text="Team Utility Pack",
        font=("맑은 고딕", 16, "bold")
    )
    title_label.pack(pady=15)

    subtitle_label = tk.Label(
        root,
        text="사용할 기능을 선택하세요",
        font=("맑은 고딕", 11)
    )
    subtitle_label.pack(pady=5)

    # 버튼들
    btn1 = tk.Button(
        root,
        text="단위 변환기 (형규)",
        width=30,
        height=2,
        command=open_unit_converter
    )
    btn1.pack(pady=5)

    btn2 = tk.Button(
        root,
        text="간단 계산기 (진철)",
        width=30,
        height=2,
        command=open_simple_calculator
    )
    btn2.pack(pady=5)

    btn3 = tk.Button(
        root,
        text="점수 평균 계산 (하린)",
        width=30,
        height=2,
        command=open_score_average
    )
    btn3.pack(pady=5)

    btn4 = tk.Button(
        root,
        text="문자열 처리 (승환)",
        width=30,
        height=2,
        command=open_string_tools
    )
    btn4.pack(pady=5)

    btn5 = tk.Button(
        root,
        text="랜덤 비밀번호 생성기 (정수)",
        width=30,
        height=2,
        command=open_password_generator
    )
    btn5.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
