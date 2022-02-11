# 01. 사전
    # 리스트를 쓰면 다음과 같이 값들을 원하는 순서로 정리해 놓을 수 있다.
my_list = [2, 3, 5, 7, 11, 13]
    # 값들을 불러오려면, 범위 안에서 정수 값들로 아래와 같이 인덱싱하면 된다.
print(my_list[1])
print(my_list[3])

    # 사전 (dictionary)
    # key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
    # type을 확인하여 보면, 'dict'로 사전 저장형임을 확인할 수 있다.

    # 이제 저장된 값을 불러와 보자
    # list 인덱싱 하듯이 대괄호 안에 키를 넣어주면 된다.
print(my_dictionary[3])

    # 이 사전에 새로운 쌍을 추가하고 싶다면 어떻게 해야 할까?
    # dictionary 키에 원하는 값을 쓰고 등호로 원하는 밸류 값을 저장해주면 된다.
my_dictionary[9] = 81
print(my_dictionary)                    # 가장 오른편에 저장됨을 확인할 수 있다.

    # 이렇게 보면 list와 dictionary는 굉장히 유사함을 알 수 있다.
    # 그렇다면 list와 dictionary의 차이점은 무엇일까?
    # list는 인덱스가 순서대로 0, 1, 2, 3, 4...  이런 식으로 진행된다.
    # 하지만 dictionary는 우리가 원하는 대로 아무 순서로 지정해 줄 수 있다. (순서 개념 x)
    # 또한 list는 인덱스가 무조건 정수형인데 반해, dictionary는 인덱스가 정수형일 필요가 없다.
my_family = {
    '엄마': '김지수',
    '아빠': '이용진',
    '아들': '이진호',
    '딸': '이지영'
}
print(my_family['아들'])
