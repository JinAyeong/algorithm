# 곡의 수, 시작 볼륨, 볼륨은 M 이하
N, S, M = map(int, input().split())
volumes = [0] + list(map(int, input().split()))
dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True
answer = -1

for i in range(1, N+1):
    vol = volumes[i]

    for j in range(M+1):
        if dp[i-1][j]:
            if 0 <= j-vol <= M:
                dp[i][j-vol] = True
            if 0 <= j+vol <= M:
                dp[i][j+vol] = True

for k in range(M, -1, -1):
    if dp[N][k]:
        answer = k
        break

print(answer)