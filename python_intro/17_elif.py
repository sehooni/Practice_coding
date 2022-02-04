# 07. elif문
# if문과 else문의 구조
    # if 조건 부분:
    #   수행부분
    # else:
    #   수행부분

# 작동 매커니즘은 다음과 같다.
    # if 온도가 10도 이하다:
    #     자켓을 입는다
    # else:
    #   if 온도가 15도 이하다:
    #       긴팔을 입는다
    #   else:
    #     반팔을 입는다.

# 그러나 조건이 많을 경우 elif를 통해서 조금 더 간결화 할 수 있다.
    # if 점수가 90점 이상이다:
    #   A를 준다
    # elif 점수가 80점 이상이다:
    #   B를 준다
    # elif 점수가 70점 이상이다:
    #   C를 준다
    # elif 점수가 60점 이상이다:
    #   D를 준다
    # else:
    #   F를 준다

# 08. 학점계산기
# 실습과제
# 학생들에게 최종 성적을 알려 주는 '학점계산기를 만들려고 합니다.
# 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요.
# 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다.
# 규칙은 다음과 같습니다.
#   A : 90점 이상
#   B : 80점 이상 90점 미만
#   C : 70점 이상 80점 미만
#   D : 60점 이상 70점 미만
#   F : 60점 미만
# print_grade 함수는 파라미터로 중간고사 점수 midterm_score과 기말고사 점수 final_score을 받고, 최종 성적을 출력합니다.
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")

# test
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 09. 이상한 수학문제 1
# 실습과제
# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만, 12의 배수는 아닌 것을 모두 출력하세요.
# 예를 들어, 16은 8의 배수이지만 12의 배수는 아니니까, 조건에 부합합니다.
# 하지만 48은 8의 배수임과 동시에 12의 배수이므로, 조건에 부합하지 않습니다.
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
        i += 1
    else:
        i += 1

# 10. 이상한 수학문제 2
# 실습과제
# 10 보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
i = 1
sum = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
        i += 1
    else:
        i += 1      # 이때 if문 조건과 else문 조건 안에 둘다 i += 1이 존재하므로, 두 문장을 없애도 if문 밖에 i += 1을 작성하면 조금더 간결하게 코드를 작성할 수 있다.

print(sum)

# 11. 약수 찾기
# 실습과제
# 정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수 입니다.
# 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써보세요.
i = 1
N = 120
count = 0
while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개 입니다.".format(N, count))

# 12. 택이의 우승 상금
# 실습과제
# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만원을 받았습니다.
# 하지만 바둑 외에는 아는 게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야 할지 물어보기로 하였습니다.
# 은행에서 근무하는 동일 아저씨는 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다.
# 1년 후인 1989년에는 5,000만원의 이자인 600만원이 더해져 5,600만원이 된다고 하면서요.
# 이 이야기를 들은 미란 아주머니는 고작 12% 때문에 생돈을 은행에 넣느냐며, 얼마 전 지어진 은마아파트를 사라고 추천하셨습니다.
# 당시 은마아파트의 매매가는 5,000만원이었죠.
# 2016년 기준 은마아파트의 매매가는 11억원인데요.
# 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여, 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을 지 판단해 보세요.
# 2016년 은행에 얼마가 있을지는 꼭 while문을 사용해서 계산해 주세요!
# 2016년에 은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.가 출력되도록 하세요.
# 반대로 은마아파트 가격이 더 크면, *원 차이로 미란아주머니 말씀이 맞습니다.가 출력되도록 하세요.
# 여기서는 if문을 사용해 주세요!
money = 50000000
year = 1988
apartment = 1100000000

while year < 2016:
    money *= 1.12
    difference = apartment - money
    year += 1

if money < apartment:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(difference)))
else:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(-1 * difference)))

# 모범 답안은 다음과 같다.
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance *= (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))

# 13. 피보나치 수열
# 실습 과제
# 피보나치 수열(Fibonacci Sequence)라고 들어 보셨나요?
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다.
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)를 더한 3입니다.
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.
previous = 0
current = 1
count = 1

while count <= 50:
    print(current)
    temp = previous           # 임시 저장소로 temp 사용 CHECK
    previous = current
    current = current + temp
    count += 1

print("혹은 이러한 방법으로도 가능하다!")

while count <= 50:
    print(current)
    previous, current = current, current + previous
    count += 1


# 14. 구구단
# 실습과제
# while문을 사용해서 구구단 프로그램을 만들어 봅시다.
# 참고로 이 문제는 '중첩 while문'이라는 개념을 사용해야 하는데요.
# 중첩 while문은 while문의 수행 부분 안에 또 다른 while문을 넣는 것을 이야기 합니다.

i = 1
n = 1
while n < 10:
    while i <= 9:
        print("{} * {} = {}".format(n, i, i*n))
        i += 1
    else:
        i = 1
    n += 1