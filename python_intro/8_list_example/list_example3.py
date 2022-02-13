# 03. 리스트 정렬
numbers = [19, 13, 37, 2, 5, 3, 11, 7, 17]
# 내림차순으로 정렬하고 싶을 떈?
# sorted 함수 이용하면 된다!!
# sorted(함수)
new_list = sorted(numbers)
print(new_list)
# 만약 역으로 정렬된 리스트를 원한다면?
new_list = sorted(numbers, reverse=True)
print(new_list)
# 기존의 함수를 아예 건들고 싶다면?
# sort 함수를 이용하면 된다!
# 함수.sort()
print(numbers.sort())
# 이러면 None이 출력되는데, sort는 아무것도 return하지 않기 때문!
# 그 대신 대상 함수 자체를 정렬하게 된다.
numbers.sort()
print(numbers)
# 여기서 거꾸로 정렬하고 싶다면?
# 마찬가지로 sort(reverse=True)를 이용!
numbers.sort(reverse=True)
print(numbers)

# 요약하자면 다음과 같다.
# sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort : 아무것도 리턴하지 않고, 기존 리스트 그 자체를 정렬
