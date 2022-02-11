# 03. 리스트와 문자열
    # 리스트와 문자열은 굉장히 비슷하다.
    # 비슷한 점을 우선 살펴보자!
    # 리스트를 인덴싱하면 다음과 같다.
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

    # 문자열 또한 리스트와 같이 인덴싱이 가능하다.
alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

    # 리스트 슬라이싱도 한번 확인하여 보자.
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

    # 문자열도 슬라이싱이 동작할까?
alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])
    # 역시나 된다!

    # 문자열을 연결하듯이 리스트도 연결할 수 있다.
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

    # len함수 또한 동작한다!
my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello world!'
print(len(my_string))

    # 그렇다면 다른 점은 어떤 것이 있을까?
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

name = 'universe'
name[0] = 'U'
print(name)
        # error가 발생한다.
        # 이유는 문자열은 수정이 불가능하다는 점 때문이다!
