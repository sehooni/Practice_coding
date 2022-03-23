# 모듈의 이름을 확인하여 보자
print('module_area의 이름: {}'.format(__name__))
    # module_area의 이름: __main__ 으로 출력됨

# 기존 area.py의 내용
    # 상수 설정
PI = 3.14


    # 원의 면적
def circle(radius):
    return PI * radius * radius


    # 정사각형의 면적
def square(length):
    return length * length

# 이때 module_area 파일이 직접 실행될 때만 아래의 내용이 나오도록 하려면?
if __name__ == '__main__':
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)
    print(square(2) == 4)
    print(square(5) == 25)
