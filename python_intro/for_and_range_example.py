# 03. range 연습
    # 실습과제
    # numbers라는 리스트가 주어졌습니다.
    # for문과 range함수를 사용하여, numbers의 인덱스와 원소를 출력해 보세요.
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for number in range(len(numbers)):
    print(number, numbers[number])

# 04. 거듭제곱
    # 실습과제
    # "2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.
    # 코드를 실행하면 2^0 = 1부터 2^10 =1 024까지 출력되어야 합니다.
for n in range(11):
    print("{}^{} = {}".format(2, n, 2 ** n))

# 05. for문으로 구구단
    # 실습과제
    # 구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.
for i in range(1, 10):
    for n in range(1, 10):
        print("{} * {} = {}".format(i, n, i * n))

# 06. 피타고라스 삼조
    # 실습과제
    # 피타고라스 삼조란, 피타고라스 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a, b, c)입니다.
    # 예를 들면, (3, 4, 5)는 피타고라스 삼조 입니다.
    # a < b < c라고 가정할 때, a + b + c = 1000을 만족하는 피타고라스 삼조 (a, b, c)는 단 하나 인데요.
# 이 경우, a * b * c는 얼마인가요?
for a in range(1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

# 07. 리스트 뒤집기
    # 실습과제
    # 리스트 원소들의 순서를 거꾸로 뒤집으려고 합니다.
    # numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for left in range(len(numbers)//2):                                  # //2가 없으면 다시 돌아서 원래 리스트가 출력된다
    right = len(numbers) - left - 1                                  # 인덱스 left와 대칭인 인덱스 right 계산

    temp = numbers[left]                                             # 위치 바꾸기
    numbers[left] = numbers[right]
    numbers[right] = temp

    # 이 방법 대신에 아래의 방법을 적용랗 수도 있다.
    # numbers[right], numbers[left] = numbers[left], numbers[right]    # 위치바꾸기
    
print("뒤집어진 리스트 : " + str(numbers))