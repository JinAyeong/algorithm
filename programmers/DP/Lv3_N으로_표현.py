def solution(N, number):

    dp = [set() for _ in range(9)]

    for i in range(1, 9):

        dp[i].add(int(str(N) * i))

        for j in range(1, i // 2 + 1):

            arr_1 = list(dp[j])
            arr_2 = list(dp[i-j])

            for x in arr_1:
                for y in arr_2:

                    # 더하기
                    dp[i].add(x + y)

                    # 빼기
                    dp[i].add(x - y)
                    dp[i].add(y - x)

                    # 곱하기
                    dp[i].add(x * y)

                    # 나누기
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)

        if number in dp[i]:
            return i

    return -1