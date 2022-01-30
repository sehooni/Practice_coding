# 상수 (constant)
PI = 3.14           # 원주율 '파이'
                    # 상수를 정의할때는 모든 글자를 대문자로 작성하는 규칙이 존재.
                    # 일반 변수와 상수를 구분 짓기 위함
                    # 실수를 하지 않기 위함! 상수는 변경되지 않기 때문에 이와 같은 규칙이 존재.

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4          # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
