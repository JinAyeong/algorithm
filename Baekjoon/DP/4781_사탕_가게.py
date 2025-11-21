'''
사탕 구매 -> 구매한 사탕의 칼로리가 더 큰 사람이 내기에서 이김
가장 칼로리의 합이 큰 경우 출력
'''

while True:

    n, m = map(float, input().split())
    n = int(n)
    m = int(round(m * 100))

    if (n, m) == (0, 0):
        break

    # 사탕 가격, 칼로리
    candy_input = [list(map(float, input().split())) for _ in range(n)]
    candy = [[int(c), int(round(p * 100))] for c, p in candy_input]

    dp = [0] * (m+1) # dp[i] = i가격으로 구매할 수 있는 사탕 칼로리의 최대값
    result = 0

    for calory, price in candy:
        for i in range(price, m+1):

            dp[i] = max(dp[i], dp[i-price] + calory)
            result = max(dp[i], result)

    print(result)