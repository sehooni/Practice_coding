# 01.while 반복문
#     무언가를 반복하기 위해 사용
#     구조는 다음과 같다.
#         while 조건부분(불린 값으로 계산되는 식(like 명제)) : # 이때 조건 부 true면 수행부분 계속 실행, false면 while 반복문 정지
#             수행부분(4칸 들여쓰기 / 반복적으로 수행하고 싶은 명령들(출력, 변수수정))
# 02. while 반복문 문법
i = 1
while i <= 3:
    print("I'm handsome!")
    i += 1

# 03. while문 연습1
# 실습과제
# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해보세요.
i = 1
while i <= 50:
    print(2*i)
    i += 1

# 04. while문 연습2
# 실습과제
# while 문을 사용하여, 100이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
i = 100
while i % 23 != 0:
    i += 1
    
print(i)