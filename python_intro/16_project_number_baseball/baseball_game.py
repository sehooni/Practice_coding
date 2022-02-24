# 01. 숫자 야구
import random


# 숫자 3개 뽑기
    # 숫자 야구 게임을 한 단계씩 완성해 나간다.
    # 먼저 정답 숫자 3개를 뽑아주는 generate_numbers 함수를 작성

    # 무작위로 0과 9사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴
def generate_numbers():
    # 숫자들이 담길 리스트 작성
    num_list = []
    while len(num_list) < 3:
        num = random.randint(0, 9)
        if num not in num_list:
            num_list.append(num)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return num_list


# 숫자 예측하기
    # 이번에는 유저에게 숫자 3개를 입력받는 take_guess함수를 작성해보자

    # 유저에게 숫자 3개를 반복적으로 입력받은 후, 유저가 입력한 숫자들을 리스트에 정리해서 리턴한다.
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    input_list = []
    while len(input_list) < 3:
        input_num = int(input("{}번째 숫자를 입력하세요: ".format(len(input_list) + 1)))

        if input_num < 0 or input_num>9:
            print("범위를 벗어나는 숫자 입니다. 다시 입력하세요.")
        elif input_num in input_list:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            input_list.append(input_num)

    return input_list


# 점수 계산
    # 이제 스트라이크 수와 볼 수를 알려주는 get_score를 작성해보자

    # 이 함수는 두 개의 파라미터를 받는다.
        # 1. guesses : 유저가 뽑은 번호 3개가 담긴 리스트
        # 2. solution : 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트

def get_score(guess, solution):
    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike += 1

    for i in range(3):
        if guess[i] in solution and guess[i] != solution[i]:
            ball += 1

    return strike, ball


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    GUESS = take_guess()
    s, b = get_score(GUESS, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))


# # 작동 확인
# print(generate_numbers())
# print(take_guess())
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)