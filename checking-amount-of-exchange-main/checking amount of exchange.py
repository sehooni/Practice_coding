# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 코드를 입력하세요.
    return krw / 1000


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 코드를 입력하세요.
    return usd / 8 * 1000


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.
i = 0
while i < len(prices):
    prices[i] = round(krw_to_usd(prices[i]), 1)
    i += 1
# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.
i = 0
while i < len(prices):
    prices[i] = round(usd_to_jpy(prices[i]), 1)
    i += 1
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))