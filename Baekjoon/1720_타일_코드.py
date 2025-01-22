dp = [0] * 31
dp[1] = 1
dp[2] = 3
dp[3] = 3

def tile(n):
    if dp[n]:
        return dp[n]

    dp[n] = dp[n-1] + 1 + dp[n-2] + 2

    

    return dp[n]

N = int(input())

print(tile(N))