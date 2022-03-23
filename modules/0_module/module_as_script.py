# 06. 모듈을 스크립트로 사용해 보기
    # 기존의 area.py를 변형하여 스크립트로 활용할 수 있다.

# 기존 area.py의 내용
    # 상수 설정
PI = 3.14


    # 원의 면적
def circle(radius):
    return PI * radius * radius


    # 정사각형의 면적
def square(length):
    return length * length


# circle 함수와 square 함수가 제대로 작성되었는지 확인하는 코드를 추가하여 보자
print(circle(2) == 12.56)
print(circle(5) == 78.5)
print(square(2) == 4)
print(square(5) == 25)

    # 값들이 True가 나오면 함수 정의가 제대로 되었다는 점을 알 수 있다!
    # 단, 이때 module_run.py를 다시 실행하면 마찬가지로 True가 4번 출력된다.
    # 그 이유는, 모듈을 import하게 되면, 그 파일 내의 모든 함수들을 출력하기 때문이다.
    # 그렇다면 이를 어떻게 수정해야 할까?

# __name__.py에서 이어서 설명해보자

