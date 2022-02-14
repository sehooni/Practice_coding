# 01. 모듈(미리 만들어놓은 모듈 이용)
    # 기본 꼴(1)
# import module_calculator as calc

    # 조금 더 쉽게 작성할 수도 있다.(2)
# from module_calculator import add, multiply, subtract

    # 함수 모두를 불러오고 싶다면? (모든 함수 불러오기)
from module_calculator import *
        # 그러나 이 방법은 추천하지 않는 방식
        # 그 이유는, 함수들의 출처가 불분명해지기 때문이다.
        # 따라서 1번 방식이나 2번 방식을 추천

    # 모듈이름을 쓰고,.후에 쓰고 싶은 함수 작성
# print(calc.add(2, 5))
# print(calc.multiply(3, 7))

print(add(2, 5))
print(multiply(3, 7))
print(subtract(3, 7))

    # 다음과 같은 모듈 데이터 분석에서 많이 사용
import numpy as np
import pandas as pd