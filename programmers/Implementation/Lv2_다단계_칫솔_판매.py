def solution(enroll, referral, seller, amount):

    n = len(enroll)
    name_idx = {enroll[i]: i for i in range(n)}  # 판매원 인덱스
    sale = [0] * n

    for i in range(len(seller)):
        name = seller[i]
        cur_profit = amount[i] * 100

        while name != "-":
            name_i = name_idx[name]
            ten = cur_profit // 10

            sale[name_i] += cur_profit - ten  # 현재 판매자 수익 갱신

            if ten < 1:
                break

            refer = referral[name_i]  # 추천인 이름
            if refer == "-":  # 추천인이 없으면 break
                break

            name = refer  # 다음 추천인으로 이동
            cur_profit = ten  # 추천인에게 수수료 전달

    return sale


#--------------------------------------------------------------------
# 실패

# 각 seller 순회하면서 amount * 100 할당
# 가입자 enroll 거꾸로 순히하면서 referral에게 10% 할당

def solution(enroll, referral, seller, amount):  # 판매원 이름, 각 판매원의 추천인 이름, 판매한사람, 판매량

    n = len(enroll)
    name_idx = {enroll[x]: x for x in range(n)}
    sale = [0] * n

    # 순수 판매량 저장
    for i, sell in enumerate(seller):
        idx = name_idx[sell]
        sale[idx] += amount[i] * 100

    for j in range(n - 1, -1, -1):
        cur = enroll[j]  # 판매자 이름
        refer = referral[j]  # 추천인 이름

        # 추천인의 수익에 판매자 수익의 10% 떼어주기
        ten_percent = sale[name_idx[cur]] // 10
        sale[name_idx[cur]] -= ten_percent

        if refer != '-':
            sale[name_idx[refer]] += ten_percent

    return sale