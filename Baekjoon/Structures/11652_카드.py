N = int(input())

cards = {}
result = -1
result_cnt = -1

for _ in range(N):
    card = int(input())

    # 카드 세기
    if card in cards:
        cards[card] += 1

    else:
        cards[card] = 1

    # 한장 셀때마다 result 검사
    if cards[card] > result_cnt:
        result_cnt = cards[card]
        result = card

    elif cards[card] == result_cnt:
        if card < result:
            result_cnt = cards[card]
            result = card

print(result)