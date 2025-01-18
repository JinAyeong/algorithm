# 다른 나무로 순간이동 가능
# result = 자두가 받을 수 있는 자두의 최대 수

T, W = map(int, input().split()) # T초동안 떨어지는 자두, 최대 W번 이동
plums = [0] + [int(input()) - 1 for _ in range(T)]

# 기억해야할것 : 현재 위치, 이동 횟수

dp = [[[0, 0] for _ in range(W+1)] for _ in range(T+1)] #[t초][이동횟수][나무 번호]

if plums[1] == 0:
    dp[1][0][0] = 1
else:
    dp[1][0][1] = 0

for t in range(2, T+1):

    for w in range(W):
        # 자리 이동
        if plums[t] == 0:
            dp[t][w][0] = dp[t-1][w-1][1] + 1
            dp[t][w][1] = dp[t - 1][w - 1][0]
        else:
            dp[t][w][0] = dp[t-1][w-1][1]
            dp[t][w][1] = dp[t - 1][w - 1][0] + 1

        # 자리 이동 x
        if plums[t] == 0:
            dp[t][w][0] = dp[t-1][w-1][0] + 1
            dp[t][w][1] = dp[t - 1][w - 1][1]
        else:
            dp[t][w][0] = dp[t-1][w-1][0]
            dp[t][w][1] = dp[t - 1][w - 1][1] + 1

for lin in dp:
    print(*lin)