# 포도주 세 잔 연속 선택 불가능
# [0] 현재 포도주 선택 안 함, [1] 현재 포도주 한 잔 선택, [2] 현재 포도주 두 잔 연속 선택

n = int(input())
wine = [0] + list(int(input()) for _ in range(n))

# dp = [[0, 0, 0] for _ in range(n+1)]
# dp[1][1] = wine[1]
# 필요한 값은 이전 포도주 정보 -> 배열 없이 prev 변수에 저장
prev_0, prev_1, prev_2 = 0, wine[1], 0

for i in range(2, n+1):

    # # 현재 포도주 선택 안함
    # dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    cur_0 = max(prev_0, prev_1, prev_2)

    # # 현재 포도주 하나만 선택 (앞의 포도주 선택 안한 [0]만 선택)
    # dp[i][1] = dp[i-1][0] + wine[i]
    cur_1 = prev_0 + wine[i]

    # # 현재 포도주까지 두개 연속 선택
    # dp[i][2] = dp[i-1][1] + wine[i]
    cur_2 = prev_1 + wine[i]

    # 이전 상태 갱신
    prev_0, prev_1, prev_2 = cur_0, cur_1, cur_2


print(max(prev_0, prev_1, prev_2))