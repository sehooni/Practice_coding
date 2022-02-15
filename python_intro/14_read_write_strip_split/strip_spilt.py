# 01. 파일 읽기
    # open 함수를 통해 파일 열기
        # 첫번쨰 파라미터: 파일이름
        # 두번째 파라미터: 문자열 'r' (read의 약자로 읽는다는 의미)
            # 작성하고 싶을 땐, 'w' (write의 약자로 쓴다는 의미)
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    # UnicodeDecoderError 발생 시, 인코딩의 문제로 문자열 다음에 바꿔주면 됨.

    # print(type(f))
    #     # <class '_io.TextIOWrapper'> : for문을 쓰면 list와 비슷하게 사용 가능
    for line in f:
        print(line)


# 02. strip
    # console에 출력값이 나오고 그다음 빈줄이 나오고... 이렇게 출력이 되는데 왜 그런걸까?
    # data값을 보면 \n이 들어가 있기 때문에 출력하면 엔터가 나오는거고, print문이 한번 더 자동으로 엔터를 치기 때문에 이와같이 출력
    # 예를 들자면 다음과 같다
print("Hello")
print("Hello\n")
print("Hello")
    # 이를 해결하기 위해 strip 사용
    # 어떤 문자열에서 앞뒤로 있는 화이트 스페이스를 없애줌
print("                  abc      def            ".strip())
print("          \t      \n        abc      def\n\n\n        ".strip())
    # 중간에 있는 화이트 스페이스는 사라지지 않음


    # 자 이제 1에서 적용한 데이터를 strip으로 처리해보자
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
   for line in f:
        print(line.strip())


# 03. split
    # 기준 파라미터를 기준으로 나눠서 list에 저장
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))
full_name = "Kim, Yuna"
print(full_name.split(", "))
    # 이 값들을 사용하기 위해서는 다음과 같이 작성
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name, last_name)


    # 이번에는 아예 다른 상황을 살펴보자
print("       \n\n       2      \t       3 \n          5 7 11    \n\n".split())


    # 마지막으로 주의사항을 살펴보자
numbers = "       \n\n       2      \t       3 \n          5 7 11    \n\n".split()
print(int(numbers[0]) + int(numbers[1]))
        # 출력되는 값은 문자열이므로 형변환을 해줘야한다는 점을 유의하자