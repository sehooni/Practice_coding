# 01. 로또 시뮬레이션
import random


# 번호 뽑기
    # 아래 함수는 파라미터로 정수 n을 받는다.
    # 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴
def generate_numbers(n):
    lotto_list = []
    while len(lotto_list) < n:
        number = random.randint(1, 45)
        if number not in lotto_list:
            lotto_list.append(number)

    return lotto_list


# 당첨 번호 뽑기

# # 너무 어렵게 생각하지 말자........ 밑에 코드는 본인이 일일히 수 작업한 코드 이나,
# winning_list = []
# def draw_winning_numbers():
#     while len(winning_list) < len(lotto_list):
#         win_number = random.randint(1, 45)
#         if win_number not in winning_list:
#             winning_list.append(win_number)
#             winning_list.sort()
#
#     bonus = random.randint(1,45)
#     if bonus not in winning_list:
#         winning_list.append(bonus)
#
#     return winning_list


# 조금 더, 아니 훨씬 간결하게 코드 작성이 가능.
def draw_winning_numbers():
    winning_list = generate_numbers(7)
    return sorted(winning_list[:6]) + winning_list[6:]


# 겹치는 번호 개수 카운트
def count_matching_numbers(lotto_list, winning_list):
    # 요소 비교 조건문
    count = 0

    for num in lotto_list:
        if num in winning_list:
            count = count + 1

    return count

# 당첨금 확인
def check(lotto_list, winning_list):
 # 초기 버전
    # if count_matching_numbers(lotto_list, winning_list[0:6]) == 6:
    #     return 1000000000
    # elif count_matching_numbers(lotto_list, winning_list[0:6]) == 5 and count_matching_numbers(lotto_list, winning_list[6:]) == 1:
    #     return 50000000
    # elif count_matching_numbers(lotto_list, winning_list[0:6]) == 5:
    #     return 1000000
    # elif count_matching_numbers(lotto_list, winning_list[0:6]) == 4:
    #     return 50000
    # elif count_matching_numbers(lotto_list, winning_list[0:6]) == 3:
    #     return 5000
    # else:
    #     return 0

 # 조금 더 간결하게
    count = count_matching_numbers(lotto_list, winning_list[:6])
    bonus_count = count_matching_numbers(lotto_list, winning_list[6:])
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# # 정상적으로 작동하는지 확인
# print(generate_numbers(6))
# print(draw_winning_numbers())
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
