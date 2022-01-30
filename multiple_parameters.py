# 파라미터를 다중으로 사용하기
    # 값을 2개 받기
def print_sum(a, b):
    print(a + b)

print_sum(7, 3)

    # 값을 3개 받기
def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 9)

    # 파라미터가 달라도 똑같이 동작
def print_sum(num_1, num_2, num_3):
    print(num_1 + num_2 + num_3)

print_sum(7, 3, 2)

# 예제 (세 수의 곱)
def multiply_three_numbers(a, b, c):
    print(a * b * c)

    # 테스트 코드
multiply_three_numbers(7, 3, 5)
multiply_three_numbers(21, 4, 9)
multiply_three_numbers(-7, 6, 3)