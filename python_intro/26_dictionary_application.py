# 03. 사전 활용법
my_family = {
    '엄마': '김지수',
    '아빠': '이용진',
    '아들': '이진호',
    '딸': '이지영'
}

    # 정의해놓은 사전에서 어떤 값들이 있는지 목록을 알고 싶을 때
    # 사전.values() 사용하면 된다.
print(my_family.values())
    # 사전에서 특정 값을 확인하고 싶을 때
print('이용진' in my_family.values())
print('이수혁' in my_family.values())
    # 사전에서 반복문을 돌리고 싶으면?
    # 아래와 같이 코드를 돌리면, 리스트에서 for문을 돌리듯이 작동하게 된다.
for value in my_family.values():
    print(value)

    # 정의해놓은 사전에서 key 목록을 불러오고 싶다면?
print(my_family.keys())
    # 이걸 또 반복문에 사용할 수 있다.
for key in my_family.keys():
    print(key)

    # 이걸 살짝 응용해보자.
for key in my_family.keys():
    value = my_family[key]
    print(key, value)
    # 위에서는 두 단계에 걸쳐서 키와 밸류 쌍을 불러왔는데, 이를 한 단계로 만들 수 있다.
for key, value in my_family.items():
    print(key, value)
