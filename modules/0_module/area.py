# 02. 모듈 사용하기
    # area 모듈에는 원의 면적을 구하는 함수와 정사각형의 면적을 구하는 함수를 넣어줄 것이다.

# 상수 설정
PI = 3.14


# 원의 면적
def circle(radius):
    return PI * radius * radius


# 정사각형의 면적
def square(length):
    return length * length