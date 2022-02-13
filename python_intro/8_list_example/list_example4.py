# 04. 리스트 인덱싱 연습
print("<4. 실습>")
print("-"*25)
# 실습과제
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉쥬" ]
# greetings 리스트의 원소를 모두 출력하는 프로그램을 작성해보세요.
# while문과 리스트의 개념을 활용
i = 0
while i <= 6:
    print(greetings[i])
    i += 1

# 조금 더 간결화 하자면 다음과 같다.
print("-"*25)                                                 # 우선 출력창 깔끔하게 만들기(선택사항)
print("<조금 더 간결화 한 version>")
print("-"*25)

i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1

print("-"*25)                                                 # 우선 출력창 깔끔하게 만들기(선택사항)
print("<5. 실습>")
print("-"*25)

# 05. 온도 단위 바꾸기
    # 실습과제
    # 화씨 온도를 섭씨온도로 바꾸어주는 프로그램을 만들려고 합니다.
    # 섭씨와 화씨의 관계식은 다음과 같습니다.
    # 섭씨 = ((화씨 - 32) * 5 ) / 9
    # 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써야한다.
    # 이 함수를 파라미터로 화씨온도 fahrenheit를 받고 변환된 섭씨 온도를 리턴 합니다.
# 화씨 온도를 섭씨 온도로 변환하여 주는 함수
import numpy as np                                             # list나 array와 같은 객체에서 round함수를 사용하기 위해 numpy import

def fahrenheit_to_celsius(fahrenheit):
    celsius = ((fahrenheit - 32) * 5)/ 9
    return np.round(celsius, 1)                                # return하는 celsius 값 소수점 아래 두번째에서 반올림 하도록 설정

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트 : " + str(temperature_list))              # 화씨 온도 리스트 출력

# 리스트의 값들을 화씨에서 섭시로 변환하는 코드
i = 0
celsius_list = []
while i < len(temperature_list):                                # 화씨 온도 리스트에 들어가 있는 횟수까지 반복
    fahrenheit = temperature_list[i]                            # 함수에 적용하기 위해 각 인덱스 요소 불러와 변환
    celsius_list.append(fahrenheit_to_celsius(fahrenheit))      # 섭씨 온도 리스트에 삽입
    i += 1                                                      # while 문 반복

print("섭씨 온도 리스트 :" + str(celsius_list))

print("-"*25)                                                   # 우선 출력창 깔끔하게 만들기(선택사항)
print("<5. 모범답안>")
print("-"*25)

# 모범 답안은 다음과 같다.
# 차이점을 살펴보자면, 확실히 더 간결하며, 따로 리스트를 만들어 주는 것이 아닌
# 리스트 자체를 바로 수정하여 만들어 준다.
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))             # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))             # 섭씨 온도 출력

print("-"*25)                                                   # 우선 출력창 깔끔하게 만들기(선택사항)
print("<6. 실습>")
print("-"*25)

# 06. 환전 서비스
    # 실습 과제
    # 구매하고 싶은 물건들의 가격을 리스트에 정리해 두었습니다.
    # prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
    # 가격의 단위는 모두 원화. 이 물건들의 가격을 미국 달러로 하면 얼마인지, 그리고 일본 엔화로 하면 얼마인지 확인해 보려고 합니다.
    # 해야 할 일은 크게 2가지 입니다.
    # 함수 작성 & 반복문을 통해 리스트 요소들 변환
    # 먼저 한국 원화를 미국 달러로 변환해 주는 krw_to_usd함수, 그리고 미국 달러를 일본 엔화로 변환해 주는 usd_to_jpy함수를 써야 합니다.
    # krw_to_usd함수는 파라미터로 원화 krw을 받아서 변환된 미국 달러 앤수로 리턴해 줍니다.
    # 마찬가지로 usd_to_jpy함수는 파라미터로 달러 usd를 받아서 변환된 일본 엔화 액수를 리턴해 주는 거죠.
    # 참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정합니다.
    # 반복문을 사용해서 리스트의 요소들을 각각 다른 화폐로 변환해야 하는데요.
    # 그 과정에서 krw_to_usd 함수와 usd_to_jpy 함수를 활용하면 됩니다.
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
def krw_to_usd(krw):                                             # 원화를 달러로
    usd = krw / 1000
    return usd

def usd_to_jpy(usd):                                             # 달러를 엔화로
    jpy = usd * 1000 / 8
    return jpy

i = 0
print("한국 화폐 : " + str(prices))                               # 한국 화폐 출력

while i < len(prices):                                           # list 달러화
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i += 1
print("미국 화폐 : " + str(prices))                               # 미국 화폐 출력

i = 0
while i < len(prices):
    prices[i] = round(usd_to_jpy(prices[i]), 1)                  # list 엔화화
    i += 1
print("일본 화폐 : " + str(prices))                               # 일본 화폐 출력

print("-"*25)                                                    # 우선 출력창 깔끔하게 만들기(선택사항)
print("<7. 실습>")
print("-"*25)

# 07. 리스트 함수 활용하기
    # 실습 과제
    # 리스트 함수를 활용하여 아래의 지시 사항을 따르세요.
    # 1. numbers라는 빈 리스트를 만들고 리스트를 출력한다.
    # 2. append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트 출력
    # 3. numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
    # 4. numbers 리스트의 인덱스 0자리에 20이라는 수를 삽입한 후 출력한다.
    # 5. numbers 리스트를 정렬한 후 출력한다.
numbers = []
print(numbers)                                                   # 1번 해결

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)                                                   # 2번 해결

i=0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    # i += 1                                                     # 이 코드로 하면 리스트의 홀수 번째 요소를 지우게 된다.
    else:                                                        # 이 코드로 하면 리스트 내 홀수인 요소를 지우게 된다.
        i += 1
print(numbers)                                                   # 3번 해결

numbers.insert(0, 20)
print(numbers)                                                   # 4번 해결

numbers.sort()
print(numbers)                                                   # 5번 해결