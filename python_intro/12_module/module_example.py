# 02. 스탠다드 라이브러리
    # 자주 쓸 법한 모듈들은 미리 설정되어 있음.
    # 이것을 바로 standard library (표준 라이브러리)라고 지칭함.
    # 자세히는 말고 어떠한 모듈들이 있는지 한번 체크해보자
import math
    # math 모듈은 스탠다드 라이브러리에 기본으로 있는 모듈
print(math.log10(100))
print(math.cos(0))
    # 함수만 있는 것이 아닌 변수도 저장되어 있음
print(math.pi)


import random
    # random 모듈은 랜덤한 값을 사용하고 싶을 때 사용
print(random.random())
    # 0과 1 사이의 랜덤한 값을 호출


import os
    # os 모듈은 operating system의 약자로, 운영체제를 의미
    # 파이썬으로 우리의 운영체제를 조작하기 위해서 사용
print(os.getlogin())
    # 현재 컴퓨터에 어떤 계정으로 로그인 되어있는지 제시
print(os.getcwd())
    # 현재 이 파일이 있는 폴더의 경로를 받아올 수 있다.


import datetime

today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

