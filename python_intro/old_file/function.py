# 변수는 값을 저장, 함수는 명령을 저장함
def hello(): # 함수의 헤더 : 함수 정의의 첫 줄
    print("Hello!")
    print("Welcome to Codeit!")

hello() # 헤더 및의 정의를 실행하게 됨.

# 예제 (카페모카 레시피)
def cafe_mocha_recipe():
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")


    # 테스트 코드
cafe_mocha_recipe()
cafe_mocha_recipe()

# 예제 (짝수? 홀수? _추상화 문제)
def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

# 예제 (거스름돈 계산기)
def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand = change // 50000
    ten_thousand = (change % 50000) // 10000
    five_thousand = (change % 10000) // 5000
    thousand = (change % 5000) // 1000

    print(f"50000원 지폐 : {fifty_thousand}장")
    print(f"10000원 지폐 : {ten_thousand}장")
    print(f"5000원 지폐 : {five_thousand}장")
    print(f"1000원 지폐 : {thousand}장")

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
