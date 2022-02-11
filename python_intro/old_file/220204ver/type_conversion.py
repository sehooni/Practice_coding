# 자료형 : 06. 형 변환
# 형 변환 (Type Conversion 혹은 Type Casting) : 값을 한 자료형에서 다른 자료형으로 바꾸는 것
print(int(3.8))
    # int는 integer. 즉 정수의 줄임말로 소수를 정수로 바꿔줌
print(float(3))
    # float는 floating point. 즉 소수의 줄임말로 정수를 소수로 바꿔줌
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))
    # 문자를 정수로 바꿈
    # 반대로 정수를 문자로 바꾸는 과정은 다음과 같다. : str사용
print(str(2) + str(5))
    # str은 string. 즉 문자열의 줄임말로 괄호안의 값을 문자열로 바꿔줌

# 예시
age = 26
print('제 나이는 ' + str(age) + '살입니다.')

# 단 논리적으로 말이 되야 변환이 진행됨에 유의
