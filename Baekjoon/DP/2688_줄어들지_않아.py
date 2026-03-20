T = int(input())

dp = [[-1] * 10 for _ in range(1001)] # [n][i] : n의 자리수에서 i숫자가 올 수 있는 경우의 수
dp[1] = [1] * 10

def solve(n):
    if dp[n][0] != -1:
        return sum(dp[n])
    
    solve(n-1)
    
    for i in range(10):
        dp[n][i] = sum(dp[n-1][i:])
    
    return sum(dp[n])

solve(64)
    
for _ in range(T):
    n = int(input())
    print(sum(dp[n]))