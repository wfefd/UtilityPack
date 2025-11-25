# unit_converter_hyungkyu.py

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
    },
    "면적": {
        "제곱미터 (m²)": 1.0,
        "헥타르 (ha)": 10_000.0,
        "제곱킬로미터 (km²)": 1_000_000.0,
    },
    "부피": {
        "밀리리터 (mL)": 1e-6,
        "리터 (L)": 1e-3,
        "세제곱미터 (m³)": 1.0,
    },
    "속도": {
        "미터/초 (m/s)": 1.0,
        "킬로미터/시 (km/h)": 1000.0 / 3600.0,
    },
    "시간": {
        "초 (s)": 1.0,
        "분 (min)": 60.0,
        "시간 (h)": 3600.0,
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


def _choose_from_list(items, prompt: str):
    """리스트에서 번호로 선택받는 간단한 유틸"""
    while True:
        print(prompt)
        for idx, item in enumerate(items, start=1):
            print(f"  {idx}. {item}")
        choice = input("번호를 입력하세요 (q: 취소): ").strip()

        if choice.lower() == "q":
            return None

        if not choice.isdigit():
            print("숫자를 입력하세요.\n")
            continue

        idx = int(choice)
        if 1 <= idx <= len(items):
            return items[idx - 1]
        else:
            print("범위에 없는 번호입니다.\n")


def main():
    """터미널에서 실행되는 단위 변환기"""
    print("=== 단위 변환기 - 형규 ===")
    print("길이 / 면적 / 부피 / 속도 / 시간 단위 변환 (축소 버전)")
    print("종료하려면 언제든지 q 를 입력하세요.\n")

    while True:
        categories = list(UNIT_DATA.keys())
        category = _choose_from_list(categories, "[카테고리 선택]")
        if category is None:
            print("프로그램을 종료합니다.")
            break

        units = list(UNIT_DATA[category].keys())

        from_unit = _choose_from_list(units, f"[{category}] From 단위 선택")
        if from_unit is None:
            print("카테고리 선택으로 돌아갑니다.\n")
            continue

        to_unit = _choose_from_list(units, f"[{category}] To 단위 선택")
        if to_unit is None:
            print("카테고리 선택으로 돌아갑니다.\n")
            continue

        # 값 입력
        while True:
            raw = input(f"\n변환할 값 ({from_unit}) 을 입력하세요 (q: 취소): ").strip()
            if raw.lower() == "q":
                print("현재 변환을 취소하고 카테고리 선택으로 돌아갑니다.\n")
                break

            try:
                value = float(raw)
            except ValueError:
                print("숫자 형식이 올바르지 않습니다. 다시 입력하세요.\n")
                continue

            try:
                result = convert_value(category, from_unit, to_unit, value)
            except Exception as e:
                print(f"오류: {e}")
                break

            print(f"\n결과: {value:g} {from_unit} = {result:.10g} {to_unit}\n")
            # 한 번 더 같은 조합으로 계산할지 여부
            again = input("같은 단위 조합으로 다시 계산할까요? (y/n): ").strip().lower()
            if again != "y":
                print()
                break


if __name__ == "__main__":
    main()
