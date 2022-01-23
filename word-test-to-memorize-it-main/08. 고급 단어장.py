import random

vocab = {}
with open('vocabulary.txt','r', encoding='UTF-8') as f:
    for voca in f:
        data = voca.strip().split(' : ')
        english_word = data[0]
        korean_word = data[1]
        vocab[english_word] = korean_word


        keys = list(vocab.keys())
        while True:
            index = random.randint(0, len(keys)-1)
            english_word = keys[index]
            korean_word = vocab[english_word]

            test = input('{} : '.format(korean_word))
            if test == 'q':
                break

            if test == english_word:
                print("맞았습니다!\n")
            else:
                print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
