# 04. 코딩닭
    # 실습과제
    # data 폴더에 있는 'chicken.txt'파일은 제가 운영하는 치킨집'코딩닭'의 12월 매출이 정리되어 있다.
    # : 의 왼쪽에는 해당 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀있다.
    # data폴더의 chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코딩닭의 하루 평균 매출을 출력하자.
    # 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 된다.
    # 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일 아닐 수도 있다.
    # 이 점을 고려해서 확장성 있는 코드를 작성하세욤

# 총 매출 초기 값 0으로 설정
total_benefit = 0

# 데이터 오픈
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for datePrice in f:
        # 불필요한 엔터 없애기
        price = datePrice.split()

        # 일자 데이터 분리
        date_data = int(price[0].strip("일:"))

        # 매출 누적 합산
        total_benefit += int(price[1])

    # 해당 달 일수 확인
    print(date_data)

    # 월 매출 계산
    print(total_benefit)

    # 하루 평균 매출 계산
    daily_benefit = total_benefit / date_data
    print(daily_benefit)

