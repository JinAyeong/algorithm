N, K = map(int, input().split())
coffees = list(map(int, input().split()))

dp = [float('inf')] * (K + 1)
dp[0] = 0

for c in coffees:
    # 전체 카페인을 하나씩 거꾸로 순회하면서 현재 커피를 마실 경우 커피 수의 최솟값 갱신
    for i in range(K, c - 1, -1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[K] if dp[K] != float('inf') else -1)