N, K = map(int, input().split()) # N개의 커피, K만큼의 카페인
coffees = list(map(int, input().split()))
coffees.sort()

dp = [float('inf')] * (K + 1)
dp[K]=0

for i in range(N):

    if 0 <= K - coffees[i]:
        dp[i] = min()

print(dp)