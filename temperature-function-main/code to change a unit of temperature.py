# 온도 단위 바꾸기 문제
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    print({}.format(celsius = (fahrenheit - 32) * 5 / 9))
    # 코드를 입력하세요.


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
i = 0
while i < 6:
    fahrenheit = temperature_list[i]
    del temperature_list[i]
    celsius = round((fahrenheit - 32) * 5 / 9, 1)
    temperature_list.insert(i, celsius)
    i += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
