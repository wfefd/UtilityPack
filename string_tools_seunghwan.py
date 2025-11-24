# string_tools_seunghwan.py

def to_upper(text: str) -> str:
    """문자열을 모두 대문자로 변환"""
    return text.upper()


def to_lower(text: str) -> str:
    """문자열을 모두 소문자로 변환"""
    return text.lower()


def capitalize_first(text: str) -> str:
    """문자열의 첫 글자만 대문자로 변환"""
    return text.capitalize()


def swap_case(text: str) -> str:
    """대문자는 소문자로, 소문자는 대문자로 변환"""
    return text.swapcase()


def remove_spaces(text: str) -> str:
    """모든 공백 제거"""
    return text.replace(" ", "")


def count_vowels(text: str) -> int:
    """문자열에서 모음 개수 세기"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_string(text: str) -> str:
    """문자열 뒤집기"""
    return text[::-1]


if __name__ == "__main__":
    # 간단한 테스트
    sample = "Hello World"
    print("Upper:", to_upper(sample))
    print("Lower:", to_lower(sample))
    print("Capitalize:", capitalize_first(sample))
    print("Swapcase:", swap_case(sample))
    print("No spaces:", remove_spaces(sample))
    print("Vowels:", count_vowels(sample))
    print("Reversed:", reverse_string(sample))
