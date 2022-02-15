# 06. 단어장 만들기
    # 실습과제
    # 영어 강사 Max는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 한다.
    # 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리한다.
    # 사용자가 새로운 단어와 뜻을 입력할 때마다 vocabuary.txt에 작성되는 것
    # 사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료된다.
    # 사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 한다.

# 프로그램 작성

with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
    while True:
        # 영어 단어 입력
        eng_word = input("영어 단어를 입력하세요: ")
        # q 입력시 종료
        if eng_word == 'q':
            break

        # 한국어 뜻 입력
        kor_word = input("한국어 뜻을 입력하세요: ")
        # q 입력시 종료
        if kor_word == 'q':
            break

        f.write('{}: {}\n'.format(eng_word, kor_word))
