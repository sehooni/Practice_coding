# 08. 고급 단어장
    # 실습과제
        # 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었죠?
        # 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 하네요.... 개발자의 삶이란..
        # 이번에는 random모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꾸세요.
        # 같은 단어를 여러번 물어봐도 괜찮으며. 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행되도록 해보자구요.

#  random 모듈 임포트 및 프로그램 작성
import random


# dictionary 이용
voca_dictionary = {}


with open('vocabulary.txt', 'r',encoding='UTF-8') as f:
    # vocabulary.txt를 list와 같이 이용해서 사전 voca_dictionary를 정리하기
    for word in f:
        voca = word.strip().split(": ")
        eng_word, kor_word = voca[0], voca[1]
        voca_dictionary[eng_word] = kor_word

# 사전 voca_dictionary에서 단어목록 key 받아오기
keys = list(voca_dictionary.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys)-1)
    eng_word = keys[index]
    kor_word = voca_dictionary[eng_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(kor_word))

    # q 입력시 종료
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == eng_word:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(eng_word))