N, T = map(int, input().split()) # 단원 수, 총 공부시간
arr = [list(map(int, input().split())) for _ in range(N)] # 공부시간 K, 획득 점수 S
dp = [0] * (T+1) # t 시간만큼 공부했을 때 얻을 수 있는 최대 점수

# 각 단원은 순회하면서 그 단원을 선택할 수 있는 시간을 고려하며 최대점수 갱신
for K, S in arr:
    for t in range(T, K - 1, -1): # 가능한 최대 시간부터 거꾸로 순회함녀서 -> 거꾸로 순회해야 중복 계산 방지
        dp[t] = max(dp[t-K] + S, dp[t]) # [현재 단원 선택 / 선택하지 않음] 중에 더 큰 값 선택

print(dp[T])