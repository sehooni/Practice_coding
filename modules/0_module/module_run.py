# 05. 스크립트 vs 모듈
# 본 코드는 area 모듈의 함수를 불러와 실행하여 준다.
    # 본 파일은 area.py 와 module_run.py로 구성되어 있다.

import area

x = float(input('원의 반지름을 입력해 주세요: '))
print('반지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))

# 스크립트
    # 프로그램을 작동시키는 코드를 담은 실행 용도의 파일
    # 즉 module_run.py는 스크립트라고 할 수 있다.
# 모듈
    # 프로그램에 필요한 변수들이나 함수들을 정의해 놓은 파일
    # 즉 area.py가 모듈로서 실행이 되는 것이다.

