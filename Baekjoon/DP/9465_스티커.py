T = int(input())

def solve(n, stickers):

    dp = [0, 0, 0]
    dp[0] = stickers[0][0]
    dp[1] = stickers[1][0]

    for i in range(1, n):
        up, down, none_select = dp

        dp[0] = stickers[0][i] + max(down, none_select)
        dp[1] = stickers[1][i] + max(up, none_select)
        dp[2] = max(up, down, none_select)

    return max(dp)

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    print(solve(n, stickers))