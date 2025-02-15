# 1 : 1가지 (1)
# 2 : 2가지 (2, 1+1)
# 3 : 4가지 (3, 2+1, 1+2, 1+1+1)

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    print(dp[n] % 1000000009)


#----------------------------------------------------------
# 실패 코드
# 원인 1. 매 테스트케이스마다 dp 새로 계산 (시간초과)
# 원인 2. dp 테이블 저장할 때 1000000009로 나눈 나머지 저장 안 함 (메모리초과), 분배법칙 적용

for tc in range(int(input())):

    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n] % 1000000009)