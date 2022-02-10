# 02. 영어 단어장
    # 실습과제
    # 해야할 일
        # 1. 단어장 만들기
        # 2. 새로운 단어들 추가
    # 1. 단어장 만들기
        # 잘 모르는 단어 네 개 입니다.
        # sanitizer: 살균제 / ambition: 야망 / conscience: 양심 / civilization: 문명
        # 이 단어들을 저장하는 사전을 만들고, 만든 사전을 vocab라는 변수에 저장하자. 단어와 뜻이 key-value로 들어가야 한다.
    # 2. 새로운 단어들 추가
        # 이미 만들어진 vocab 사전에 새로운 단어들을 추가하고 싶다. 아래 단어들을 추가하자
        # privilege: 특권 / principle: 원칙
print("< 1. 단어장 만들기>")
print('-'*12)

vocab = {
    'sanitizer':  '살균제',
    'amibition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}

print(vocab)
print('-'*12)

print("< 2. 단어장 만들기>")
print('-'*12)

vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

print(vocab)
