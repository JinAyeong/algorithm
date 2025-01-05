# 1 : 1가지 (1)
# 2 : 2가지 (2, 1+1)
# 3 : 3가지 (3, 2+1, 1+1+1)
# 4 : 4가지 (3+1, 2+1+1, 1+1+1+1, 2+2)

dp = [0] * 10001

# 1로만 정수의 합을 나타내는 경우의 수 : 1가지
for i in range(1, 10001):
    dp[i] = 1

# 1 또는 2를 포함하여 정수의 합을 나타내는 경우의 수
dp[2] += 1  # 2 추가
for i in range(2, 10001):
    dp[i] += dp[i-2]

# 1 또는 3 또는 3을 포함하여 정수의 합을 나타내는 경우의 수
dp[3] += 1  # 3 추가
for i in range(3, 10001):
    dp[i] += dp[i-3]


for tc in range(int(input())):

    n = int(input())
    print(dp[n])

#-------------------------------------------------
# 최적화
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for tc in range(int(input())):

    n = int(input())
    print(dp[n])