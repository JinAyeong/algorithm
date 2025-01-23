dp = [0] * 31
dp[1] = 1
dp[2] = 3

# 전체 배치 경우의 수 계산
for i in range(3, 31):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]


def tile(N):
    # 대칭 배치 경우의 수 계산
    if N % 2 == 0:  # N이 짝수
        center = dp[N // 2] + 2 * dp[N // 2 - 1]
    else:  # N이 홀수
        center = dp[N // 2]

    # 중복 제거된 경우의 수 계산
    return (dp[N] + center) // 2


# 입력 및 결과 출력
N = int(input())
print(tile(N))
