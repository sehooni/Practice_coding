with open('vocabulary.txt','r', encoding='UTF-8') as f:

    for voca in f:
        data = voca.strip().split(' : ')
        english_word = data[0]
        korean_word = data[1]
        while True:
            ew = input('{} : '.format(english_word))
            if ew == korean_word:
                print("맞았습니다!\n")
                break

            else:
                print("아쉽습니다. 정답은 {}입니다.\n".format(korean_word))
                break