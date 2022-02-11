# 01. for 반복문
my_list = [2, 3, 5, 7, 11]
for number in my_list:
    print(number)

# 02. range 함수
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)                        # 이건 범위가 넓어지면 너무 복잡해지므로, 등장하는 개념이 range함수

    # 파라미터 2개 버전 (start부터 stop-1까지의 범위)
    # for i in range(start, stop):
    #   print(i)

for i in range(3, 11):
    print(i)

    # 파라미터 1개 버전 (0부터 stop-1까지의 범위)
    # for i in range(stop)
    #   print(i)
for i in range(10):
    print(i)

    # 파라미터 3개 버전 (start부터 stop-1까지의 범위, 간격 step)
    # for i in range(start, stop, step):
    #   print(i)
for i in range(3, 17, 3):
    print(i)

    # 그렇다면 range함수의 장점은 무엇일까?
    # 간편함, 깔끔함, 메모리 효율성

