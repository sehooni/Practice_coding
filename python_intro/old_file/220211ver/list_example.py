# 01. 리스트(list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["세훈", "태일", "준호", "준수"] # 리스트를 구성하는 단위 = 요소

print(numbers)
print(names)

# 리스트 내의 요소들의 위치 = 인덱스
# 인덱싱(indexing)
print(names[1])                 # 요소 불러오기
print(numbers[1] + numbers[3])  # 요소를 불러와서 계산 가능

num_1 = numbers[1]
num_3 = numbers[3]
print(num_1 + num_3)            # 요소를 변수에 저장하고, 변수로 계산 또한 가능

print(numbers[-6])              # 마이너스 인덱스도 존재
print(numbers[-1])              # 이는 반대부터 불러오는 의미

# 리스트 슬라이싱 (list slicing)
print(numbers[0:4])             # 리스트의 일부분만 호출도 가능
print(numbers[2:])              # :뒤에 암것도 없으면 끝까지
print(numbers[:3])              # : 앞에 암것도 없으면 맨 앞부터 갯수만큼
new_list = numbers[:3]          # [2,3,5]
print(new_list)

# list 요소 바꾸기
numbers[0] = 7                  # 정수 7을 0번 인덱스에 삽입
print(numbers)
numbers[0] = numbers[0] + numbers[1]
print(numbers)                  # 결국 지정연산자 개념은 여기서도 유지됨

