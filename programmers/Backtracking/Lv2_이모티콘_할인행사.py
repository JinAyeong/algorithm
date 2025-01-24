# 이모티콘 할인 10, 20, 30, 40 중 하나
# 사용자는 일정 비율 이상 할인하는 이모티콘 전부 구매 -> 총액 10000원 넘으면 이모티콘플러스 가입
# return : [가입자 수, 이모티콘 매출액]
# dfs : 이모티콘 10~40까지의 할인율중 고르기
# 금액 계산 : 가입자수가 제일 많고, 그다음으로 매출액이 많으면 값 갱신

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    sale = [10 for _ in range(m)]
    answer = [0, 0]

    def dfs(i):  # 할인율 정한 수

        if i == m:

            total_amount = 0
            cnt = 0

            # 유저 한명씩 가격 계산
            for user in users:
                amount = 0
                # 이모티콘 구매 가격
                for s in range(m):
                    if sale[s] >= user[0]:
                        amount += emoticons[s] * (100 - sale[s]) // 100
                # 이모티콘 플러스 결제할지말지
                if amount >= user[1]:  # 구매
                    amount = 0
                    cnt += 1

                else:  # 구매안함
                    total_amount += amount

            # 정답 갱신
            if cnt > answer[0]:

                answer[0] = cnt
                answer[1] = total_amount

            elif cnt == answer[0]:
                if total_amount > answer[1]:
                    answer[1] = total_amount

            return

        # 이모티콘 하나씩 갱신
        for j in [10, 20, 30, 40]:
            cur = sale[i]

            sale[i] = j
            dfs(i + 1)
            sale[i] = cur

    dfs(0)

    return answer