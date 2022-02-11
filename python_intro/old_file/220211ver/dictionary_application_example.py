# 04. 사전 뒤집기
print("< 4. 사전 뒤집기>")
print('-'*12)
    # 실습과제
    # 02. 영어단어장에서 단어장 프로그램을 만들었다.
    # 하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해보려 한다.
    # 사전의 key와 value를 뒤집어 주는 함수 reverse_dit을 작성하자.
    # reverse_dict는 파라미터로 사전 dict을 받고, key와 value가 뒤집힌 새로운 사전을 리턴한다.


def reverse_dict(dict):                 # 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
    new_dict = {}                       # 새로운 사전

    # # dict의 key와 value를 뒤집어서 new_dict에 저장
    # for key in dict.keys():
    #     value = dict[key]
    #     new_dict[value] = key

    # 이를 더 쉽게하고자 한다면?
    for key, value in dict.items():
        new_dict[value] = key

    return new_dict

    # 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

    # 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

    # 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

print('-'*12)

# 05. 투표 집계하기
print("< 5. 투표 집계하기>")
print('-'*12)
    # 실습과제
    # 효신이는 매년 국회의원 선거 때마다, 용산구에서 집계 도우미 봉사를 하는데요.
    # 작년까지는 표를 손수 세다가, 올해부터는 IT시대에 더 적합한 솔루션을 개발하고자 합니다.
    # 파이썬 리스트 votes애는 용산구민들의 투표 결과가 저장되어 있습니다.
    # 리스트의 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하는 것이 목표입니다.
    # 예를 들어서 votes가 ['김유나', '박현진', '김유나']라고 가정하면, vote_counter는 {'김유나': 2, '박현진': 1}이 되어야 하는 거죠.

    # 투표 결과 리스트
votes = ['김지훈', '강윤', '이현수', '김지훈', '강윤', '강윤', '이현수', '김지훈', \
'이현수', '김지훈', '이현수', '김지훈', '김지훈', '이현수', '이현수', '이현수', '강윤', \
'강윤', '김지훈', '김지훈', '이현수', '김지훈', '김지훈', '강윤', '김지훈']

    # 후보별 득표수 사전
vote_counter = {}

    # 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    vote_counter[name] = votes.count(name)

#     # 본인은 여기서 count함수를 사용하여 계산하였으나,
#     # 정석대로면은
#         # 해당 후보(name)가 아직 vote_counter에 없는 케이스
#         # 해당 후보(name)가 이미 vote_counter에 있는 케이스
#     # 이렇게 나눠서 카운트하여 해결
# for name in votes:
#     if name in vote_counter.keys():
#         vote_counter[name] += 1
#     else:
#         vote_counter[name] = 1

    # 후보별 득표수 출력
print(vote_counter)
