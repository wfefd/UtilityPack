def main():
    user_input = (input("점수를 입력하시오: "))
    scores = list(map(float, user_input.split()))
    score_average(scores)

def score_average(scores_list):
    count = len(scores_list)
    if count == 0:
        print("입력 오류")
        return

    total = sum(scores_list)
    average = total/count
    print(f"점수 평균: {average}")

if __name__ == "__main__":
    main()
