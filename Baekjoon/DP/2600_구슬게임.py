# 구슬 통 두 개 중 하나 선택 -> 세 가지 경우의 개수로 구슬 꺼내기
# 항상 A 먼저 시작

b1, b2, b3 = map(int, input().split())  # 한번에 꺼낼 수 있는 구슬의 개수

for i in range(5):

    k1, k2 = map(int, input().split())  # 두 통 속에 담겨있는 구슬의 개수
    # b1개 뽑기, b2개 뽑기, b3개 뽑기 중에 하나 선택
    # 박스 두개중에 하나 선택

    dp = [[0] * 6 for _ in range(501)]
    dp[0] = [k1, k1, k1, k2, k2, k2]

    for j in range(1, 500):

        box_1 = True
        box_2 = True

        # 첫번째 박스 뽑기
        if dp[j-1][0] >= b1:
            dp[j][0] = dp[j-1][0] - b1
        else:
            box_1 = False

        if dp[j-1][1] >= b2:
            dp[j][1] = dp[j-1][1] - b2
        else:
            box_1 = False

        if dp[j-1][2] >= b3:
            dp[j][2] = dp[j-1][2] - b3
        else:
            box_1 = False

        # 두번째 박스 뽑기
        if dp[j - 1][3] >= b1:
            dp[j][3] = dp[j - 1][3] - b1
        else:
            box_2 = False

        if dp[j - 1][4] >= b2:
            dp[j][4] = dp[j - 1][4] - b2
        else:
            box_2 = False

        if dp[j - 1][5] >= b3:
            dp[j][5] = dp[j - 1][5] - b3
        else:
            box_2 = False

        if box_1 == False and box_2 == False and j % 2 == 1:
            print('A')
            break

        elif box_1 == False and box_2 == False and j % 2 == 0:
            print('B')
            break
