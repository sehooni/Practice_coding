# 07. 단어 퀴즈
    # 실습과제
    # 앞선 실습 과제에서 vocabulary.txt라는 파일을 만들었습니다.
    # 이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있어요.
    # 이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내 주는 프로그램을 만들려고 합니다.
    # 프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
    # 사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.
    # 문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.

# # 프로그램 작성
# with open("vocabulary.txt", "r", encoding='UTF-8') as f:
#     for voca_data in f:
#         # 불필요한 엔터 없애기
#         voca = voca_data.split()
#
#         # 한국어 뜻만 분류
#         kor_voca = voca[1].strip(": ")
#
#         # 영어단어만 분류
#         eng_answer = voca[0].strip(": ")
#
#         # 사용자 입력 받기
#         eng_word = input("{}: ".format(kor_voca))
#
#         # 조건문을 통한 정답 유무 판정
#         if eng_word == eng_answer:
#             print("맞았습니다!\n")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.\n".format(eng_answer))


# 조금 더 깔끔해지려면 for문 바로 밑 세가지 부분이 달라져야 한다.
with open('vocabulary.txt', 'r',encoding='UTF-8') as f:
    for voca_data in f:
        voca = voca_data.strip().split(": ")
        eng_word, kor_word = voca[0], voca[1]

        # 유저 입력값 받기
        guess = input("{}: ".format(kor_word))

        # 정답 확인하기
        if guess == eng_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(eng_word))