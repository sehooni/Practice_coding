# 02. 리스트 함수
numbers = []
# list 내에 몇 개의 요소가 있는지 알고 싶다면 어떻게 해야 할까?
# len 함수 : list의 요소를 알려주는 함수
print(len(numbers))
# list에 값을 추가하고 싶을 때 사용하는 함수 : append (추가 연산)
# 이때 오른쪽 끝에 값을 apppend를 이용하여 추가하게 된다.
# 함수.append(원하는 요소)
numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))

# 새로운 예시를 살펴보자.
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)
# list에서 어떠한 요소를 지우고 싶을 때는 어떻게 해야 할까?
# del이라는 함수를 사용하면 된다.
# 이떄 삭제하고 싶은 요소의 인덱스를 적어주면 된다.
# del 함수[인덱스]
del numbers[3]
print(numbers)
# 값을 원하는 위치에 삽입할 때는 어떻게 하면 될까?
# insert 함수 이용 (삽입 연산)
# 함수.insert(원하는 인덱스, 원하는 요소)
numbers.insert(4, 37)
print(numbers)