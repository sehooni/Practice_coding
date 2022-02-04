# 자료형 : 12. 불 대수
    # 불 대수 : 일상적인 논리를 수학적으로 표현한 것
    # 불 대수의 값 = 진리값으로 참 거짓 판별
        # AND OR NOT
        # 명제 : 참과 거짓이 확실한 것
        # AND 연산 : x와 y가 모두 참일 때만 x AND y가 참
        # OR 연산 : x외 y 중 하나라도 참이면 x OR y는 참
        # NOT 연산 : 반대로 뒤집어 주는 역할

# 자료형 : 13. 불린형
    # 불린 (Boolean)
print(True)
print(False)
    # 불린 연산 (and)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
    # 불린 연산 (or)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
    # 불린 연산 (not)
print(not True)
print(not False)

# 연습 문제
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)

# 연습 문제
print("hello" == "hello")
print("hello" != "hello")

# 연습 문제
print(not not True)
print(not not False)
print(7 == 7 or (4 < 3 and 12 > 10))

# 연습 문제
x = 3
print(x > 4 or not (x < 2 or x == 3))

# 예제 (짝수? 홀수? _추상화 문제)
def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))
