def get_square(x):
    return x * x # 출력값을 마지막으로 만드는 것

print(get_square(3))

y = get_square(3) # 지정연산자
print(y)

print(get_square(3) + get_square(4))

# return문의 역할
    # 함수 즉시 종료하기
    # 값 돌려주기

# return과 print의 차이
def print_square(x):
    print(x * x)

print_square(3)             # 9가 콘솔에 출력됨. print_square()라는 함수에 파라미터로 3을 넣었을 경우에 답을 프린트 해줌.
get_square(3)
print(get_square(3))
print(print_square(3))      # None이 콘솔에 출력됨
                            # print(type(print_square(3))를 해보면 print_square(3)이 NoneType으로 뜨는걸 확인할 수 있음.
                            # 따라서 print(None)으로 읽혀 None이 출력됨.

# 하나 더 예시를 들자면
def function_that_prints():
    print("I printed")

f1 = function_that_prints()

function_that_prints()

f1 # f1만 적어주면 위에서 정의한 함수를 이미 지정하였기 때문에 아무런 일도 일어나지 않는다. 따라서 단독으로 사용하기 보다는, 할당하여 사용하여 주는 것이 좋다.
print(type(f1))

# 예제 (짝수? 홀수? _추상화 문제)
def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))