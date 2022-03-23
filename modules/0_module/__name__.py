# 07. __name__ 특수 변수
    # module_as_script.py에서 보았듯이 우리의 문제는 module_run.py를 다시 실행하면 마찬가지로 True가 4번 출력된다는 점이다.
    # 그 이유는, 모듈을 import하게 되면, 그 파일 내의 모든 함수들을 출력하기 때문이다.
    # 그렇다면 이를 어떻게 수정해야 할까?
        # module_area.py와 같이 보자!

# __name__
    # 모듈의 이름을 저장해놓은 변수
    # name의 값은 python에서 알아서 지정해준다.
    # 파이썬 파일을 직접실행하면, name은 __main__으로 지정이 되고,
    # 다른 곳에서 임포트해서 사용하게 되면, 원래 모듈 이름으로 설정된다.

print('__name__ 파일 이름: {}'.format(__name__))
    # module_area의 이름: module_area
    # run 파일 실행됨
    # __name__ 파일 이름: __main__ 로 출력된다.

    # module_area.py의 코드를 가져와서 설명해보자

import module_area

# x = float(input('원의 반지름을 입력해 주세요: '))
# print('반지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))
#
# y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
# print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))

print('__name__ 파일 실행됨')


