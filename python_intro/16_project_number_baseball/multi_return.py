# 파이썬에서 여러 값을 리턴하고 싶으면 이렇게 할 수 있다.

def square_and_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube

s, c = square_and_cube(2)
print(s)
print(c)
