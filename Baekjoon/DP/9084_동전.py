for _ in range(int(input())):

    N = int(input()) # 동전 가지 수
    coins = list(map(int, input().split()))
    M = int(input()) # 만들어야할 금액

    dp = [0] * (M+1) # m원을 만드는데 가능한 방법 수

    for coin in coins:
        if coin <= M:
            dp[coin] += 1

        for i in range(coin, M+1):
            if 0 <= i - coin < M+1:
                dp[i] += dp[i-coin]

    print(dp[M])