# 05. 자릿수 합 구하기
print("< 05. 자릿수 합 구하기>")
print('-'*12)
    # 실습과제
    # 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴한다.
    # 예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3(1+2)을 리턴한다.
    # 마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4+8+6)을 리턴한다.
    # 해야할 일은 두가지 이다.
        # 1. sum_digit함수를 작성한다.
        # 2. sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.

# sum_digit 함수 작성
def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
result = 0
for i in range(1001):
    result += sum_digit(i)

print(result)

print('-'*12)


# 06. 주민등록번호 가리기
print("< 06. 주민등록번호 가리기>")
print('-'*12)
    # 실습과제
    # 주민등록번호 YYMMDD-abcdefg는 총 13자리 이다.
    # 앞의 6자리는 생년월일을 의미
        # YY = Year
        # MM = Month
        # DD = Date
    # 뒤의 7자리는 살짝 복잡
        # a = 성별
        # bc = 출샹등록지에 해당하는 지방자치단체의 고유번효
        # defg = 임의의 번호
    # 보다시피 많은 부분은 특정 규칙대로 정해져있다.
    # 즉, 몇가지 정보만 알면, 마지막 4개의 숫자 defg를 제외한 앞의 아홉자리는 쉽게 알 수 있다.
    # 따라서, 우리는 주민등록번호의 마지막 4자리 defg만 가려주는 보안프로그램을 만들려고 한다.
    # mask_security_number라는 함수를 정의
        # 이 함수는 파라미터로 문자열 security_number를 받고,
        # security_number의 마지막 4글자를 '*'로 대체한 새 문자열을 리턴.
    # 참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있다.
    # 작대기 포함여부와 상관 없이, 마지막 4글자가 '*'로 대체되어야 한다.

# # mask_security_number 함수 작성 (join함수 사용)
# def mask_security_number(security_number):
#     list_SN = list(str(security_number))
#     for i in range(1,5):
#         list_SN[-i] = '*'
#     security_number = "".join(list_SN)
#     return security_number


# mask_security_number 함수 작성 (join함수 사용x)
    # 기존 리스트에서 원소를 불런와서 스트링 데이터로 저장하게 된다!
def mask_security_number(security_number):
    security_number_list = list(security_number)

    security_str = ""
    for i in range(len(security_number_list)):
        if len(security_number_list)-4 <= i:
            security_number_list[i] = '*'
        security_str += security_number_list[i]
    return security_str


# test
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

print('-'*12)


# 07. 팰린드롬
print("< 07. 팰린드롬>")
print('-'*12)
    # 실습과제
    # "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부른다.
    # 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 한다.
    # is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴한다.
    # 예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 한다.
    # "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 한다.

# # is_palindrome 함수 작성 ([::1]사용)
# def is_palindrome(word):
#     list_word = list(word)
#     reversed_list = list_word[::-1]
#     if list_word == reversed_list:
#         return True
#     else:
#         return False


# is_palindrome 함수 작성 ([::1]사용x)
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False로 리턴하고 함수 종료
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍 일치로 판단
    return True


# Test
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

print('-'*12)
