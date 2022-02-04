# 자료형 : 08. format을 이용한 문자열 포맷팅
# 연습문제
    # 오늘은 2021년 1월 21일입니다.
year = 2021
month = 1
day = 21

print('오늘은 ' + str(year) + '년 ' + str(month) + '월 ' +  str(day) + '일입니다.')
    # 코딩의 핵심은 조금 더 간결하게 코드 짜기

    # 이떄 format을 이용
print('오늘은 {}년 {}월 {}일입니다.'.format(year, month, day))

    # 이를 조금 더 간결화할 수 있다.
date_String = '오늘은 {}년 {}월 {}일입니다.'
print(date_String.format(year, month, day))

    # 조금 더 응용하여 다음 날을 출력하고 싶다면?
print(date_String.format(year, month, day + 1))

# 자료형 : 09. format 다루기
# 연습문제
print("저는 {}, {}, {}를 좋아합니다!".format("유현", "시현", "서연"))

    # 순서 바꾸기도 가능
print("저는 {1}, {0}, {2}를 좋아합니다!".format("유현", "시현", "서연"))

# 연습문제
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))

    # 이때 num_1 / num_2 의 출력값인 0.333333333... 을 소숫점 둘째자리까지 보고 싶다면?
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))

    # 이때 num_1 / num_2 의 출력값인 0.333333333... 을 정수로 받고 싶다면?
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))

# 예제 (자료형 11. 문자열 포맷팅 연습)
    # 주어진 코드에서 wage는 1시간에 얼마 버는지를 나타내는 값이고, exchange_rate는 1달러를 한국 돈으로 바꾸면 얼마인지 나타내는 값(환율)입니다.
    # 1시간 동안 번 금액은 wage * 1의 결과값인 5달러이고, 이 금액을 한국 돈으로 환전하면 wage * 1 * exchange_rate의 결과값인 5710.8원이 되는거죠.

    # 문자열 포맷팅의 개념을 이용하여 아래의 문장들을 출력하세요.

    # 1시간에 5달러 벌었습니다.
    # 5시간에 25달러 벌었습니다.
    # 1시간에 5710.8원 벌었습니다.
    # 5시간에 28554.0원 벌었습니다.
    # 주어진 변수와 문자열 포맷팅을 반드시 이용하셔야 합니다. 그리고 원화 금액은 소수점 첫째 자리까지만 출력되어야 합니다.
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5,"달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))
