# 02. 숫자 맞히기 게임
    # 실습과제
        # 1과 20 사이의 숫자를 맞히는 게임을 만들려고 합니다.
        # random 모듈과 input함수를 활용하여 프로그램을 만들어 보세요.

    # 진행방식
        # 1. 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "가 출력됩니다.
        # 총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
        # 2. 정답을 맞히면 "축하합니다. *번 만에 숫자를 맞히셨습니다."가 출력되고 프로그램은 종료됩니다.
        # 3. 사용자가 입력한 수가 정답보다 작은 경우 "Up"이 출력되고, 입력한 수가 정답보다 큰 경우 "Down"이 출력됩니다.
        # 4. 정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, "아쉽습니다. 정답은 *입니다."가 출력되고 프로그램은 종료됩니다.
import random

# 상수 정의
answer = random.randint(1, 20)
chance = 4

# 임의로 변수 지정
guess = -1
trial = 0

while guess != answer and trial < chance:
    # guess 원하는 값 받기
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(chance-trial)))
    trial += 1

    # 값이 다를 경우 조건문 돌리기
    if guess > answer:
        print("Down")
    elif guess < answer:
        print("Up")

    # 반복문 조건(답을 고르거나, 시도 제한 횟수 도달) 성립시, 종료됨

if guess == answer:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(trial))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(answer))
