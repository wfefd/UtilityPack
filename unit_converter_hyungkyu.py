# unit_converter_hyungkyu.py
import tkinter as tk
from tkinter import messagebox

# 카테고리별 단위 정의 (값은 "해당 단위를 기본 단위로 바꾸는 계수")
# 길이: 기본 단위 = 미터 (m)
# 면적: 기본 단위 = 제곱미터 (m²)
# 부피: 기본 단위 = 세제곱미터 (m³)
# 속도: 기본 단위 = m/s
# 시간: 기본 단위 = 초 (s)

UNIT_DATA = {
    "길이": {
        "밀리미터 (mm)": 1e-3,
        "센티미터 (cm)": 1e-2,
        "미터 (m)": 1.0,
        "킬로미터 (km)": 1000.0,
        "인치 (in)": 0.0254,
        "피트 (ft)": 0.3048,
        "야드 (yd)": 0.9144,
        "마일 (mi)": 1609.344,
        "해리 (nmi)": 1852.0,
    },
    "면적": {
        "제곱밀리미터 (mm²)": 1e-6,
        "제곱센티미터 (cm²)": 1e-4,
        "제곱미터 (m²)": 1.0,
        "제곱킬로미터 (km²)": 1_000_000.0,
        "헥타르 (ha)": 10_000.0,
        "에이커 (ac)": 4046.8564224,
        "제곱인치 (in²)": 0.00064516,
        "제곱피트 (ft²)": 0.09290304,
        "제곱야드 (yd²)": 0.83612736,
        "제곱마일 (mi²)": 2_589_988.110336,
    },
    "부피": {
        "세제곱밀리미터 (mm³)": 1e-9,
        "세제곱센티미터 (cm³)": 1e-6,
        "밀리리터 (mL)": 1e-6,
        "리터 (L)": 1e-3,
        "세제곱미터 (m³)": 1.0,
        "세제곱인치 (in³)": 0.000016387064,
        "세제곱피트 (ft³)": 0.028316846592,
        "온스 (US fl oz)": 2.95735295625e-5,
        "컵 (US cup)": 0.0002365882365,
        "파인트 (US pt)": 0.000473176473,
        "쿼트 (US qt)": 0.000946352946,
        "갤런 (US gal)": 0.003785411784,
    },
    "속도": {
        "미터/초 (m/s)": 1.0,
        "킬로미터/시 (km/h)": 1000.0 / 3600.0,
        "마일/시 (mph)": 1609.344 / 3600.0,
        "노트 (kn)": 1852.0 / 3600.0,
        "피트/초 (ft/s)": 0.3048,
    },
    "시간": {
        "나노초 (ns)": 1e-9,
        "마이크로초 (µs)": 1e-6,
        "밀리초 (ms)": 1e-3,
        "초 (s)": 1.0,
        "분 (min)": 60.0,
        "시간 (h)": 3600.0,
        "일 (day)": 86400.0,
        "주 (week)": 604800.0,
    },
}


def convert_value(category: str, from_unit: str, to_unit: str, value: float) -> float:
    """카테고리/단위/값을 받아서 변환 결과를 float로 반환"""
    units = UNIT_DATA.get(category)
    if units is None:
        raise ValueError("잘못된 카테고리입니다.")

    if from_unit not in units or to_unit not in units:
        raise ValueError("지원하지 않는 단위입니다.")

    factor_from = units[from_unit]   # from_unit -> base
    factor_to = units[to_unit]       # to_unit   -> base

    base_value = value * factor_from     # 입력값을 '기본 단위'로
    result = base_value / factor_to      # 기본 단위를 목표 단위로
    return result


def main():
    # 이미 Tk가 떠 있으면 (main_menu.py에서 호출하는 경우) Toplevel 사용
    if tk._default_root is None:
        root = tk.Tk()
    else:
        root = tk.Toplevel(tk._default_root)

    root.title("단위 변환기 - 형규")
    root.geometry("480x320")

    # 상태 변수들
    category_var = tk.StringVar()
    from_unit_var = tk.StringVar()
    to_unit_var = tk.StringVar()
    value_var = tk.StringVar()
    result_var = tk.StringVar()

    # 카테고리 선택 시 단위 목록 갱신
    def update_units(*args):
        category = category_var.get()
        units = list(UNIT_DATA.get(category, {}).keys())

        if not units:
            return

        # from / to 옵션 메뉴 갱신
        from_menu = from_unit_option["menu"]
        to_menu = to_unit_option["menu"]
        from_menu.delete(0, "end")
        to_menu.delete(0, "end")

        for u in units:
            from_menu.add_command(
                label=u,
                command=lambda v=u: from_unit_var.set(v)
            )
            to_menu.add_command(
                label=u,
                command=lambda v=u: to_unit_var.set(v)
            )

        # 기본 선택값
        from_unit_var.set(units[0])
        if len(units) > 1:
            to_unit_var.set(units[1])
        else:
            to_unit_var.set(units[0])

    def on_convert():
        category = category_var.get()
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        text_value = value_var.get().strip()

        if not category:
            messagebox.showwarning("경고", "카테고리를 선택하세요.")
            return
        if not from_unit or not to_unit:
            messagebox.showwarning("경고", "단위를 선택하세요.")
            return
        if not text_value:
            messagebox.showwarning("경고", "값을 입력하세요.")
            return

        try:
            value = float(text_value)
        except ValueError:
            messagebox.showerror("오류", "숫자 형식이 올바르지 않습니다.")
            return

        try:
            result = convert_value(category, from_unit, to_unit, value)
        except Exception as e:
            messagebox.showerror("오류", str(e))
            return

        # 보기 좋게 포맷 (유효 숫자 10자리)
        result_str = f"{value:g} {from_unit} = {result:.10g} {to_unit}"
        result_var.set(result_str)

    # 위젯 배치
    title_label = tk.Label(root, text="단위 변환기", font=("맑은 고딕", 16, "bold"))
    title_label.pack(pady=10)

    # 카테고리 선택
    frame_top = tk.Frame(root)
    frame_top.pack(pady=5)

    tk.Label(frame_top, text="카테고리:", font=("맑은 고딕", 11)).grid(row=0, column=0, padx=5, pady=5)

    category_option = tk.OptionMenu(
        frame_top,
        category_var,
        *UNIT_DATA.keys()
    )
    category_option.grid(row=0, column=1, padx=5, pady=5)

    # 값 입력
    tk.Label(frame_top, text="값:", font=("맑은 고딕", 11)).grid(row=0, column=2, padx=5, pady=5)
    value_entry = tk.Entry(frame_top, textvariable=value_var, width=12)
    value_entry.grid(row=0, column=3, padx=5, pady=5)

    # 단위 선택
    frame_units = tk.Frame(root)
    frame_units.pack(pady=10)

    tk.Label(frame_units, text="From:", font=("맑은 고딕", 11)).grid(row=0, column=0, padx=5, pady=5)
    from_unit_option = tk.OptionMenu(frame_units, from_unit_var, "")
    from_unit_option.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_units, text="To:", font=("맑은 고딕", 11)).grid(row=0, column=2, padx=5, pady=5)
    to_unit_option = tk.OptionMenu(frame_units, to_unit_var, "")
    to_unit_option.grid(row=0, column=3, padx=5, pady=5)

    # 변환 버튼
    convert_button = tk.Button(root, text="변환", width=12, height=1, command=on_convert)
    convert_button.pack(pady=5)

    # 결과 표시
    result_label = tk.Label(root, textvariable=result_var, font=("맑은 고딕", 11))
    result_label.pack(pady=10)

    # 카테고리 선택 시 단위 자동 갱신 연결
    category_var.trace_add("write", update_units)

    # 초기 카테고리 설정 (길이)
    category_var.set("길이")

    # 메인 루프
    root.mainloop()


# main_menu.py에서 import해서 main() 호출할 거라면
# 아래는 그대로 두면 됨
if __name__ == "__main__":
    main()
