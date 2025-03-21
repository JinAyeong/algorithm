n = int(input())

golomb = [0, 1, 2, 2]
dp = [0] * (n+1)
dp[1] = 1
dp[2] = dp[3] = 2

if n <= 1:
    print(dp[n])
    exit(0)

for i in range(3, n+1):
    for _ in range(golomb[i]):
        golomb.append(i)
    dp[i] = golomb[i]

print(dp[n])