# 1. x += n
# 2. x *= 2
# 3. x *= 3

def solution(x, y, n):
    answer = 0

    dp = [float('inf')] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):

        # 숫자 i까지 계산할 방법이 없다면 continue
        if dp[i] == float('inf'):
            continue

        # 1. x += n
        if i + n <= y:
            dp[i + n] = min(dp[i] + 1, dp[i + n])

        # 2. x *= 2
        if i * 2 <= y:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])

        # 3. x *= 3
        if i * 3 <= y:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])

    if dp[y] == float('inf'):
        answer = -1
    else:
        answer = dp[y]

    return answer