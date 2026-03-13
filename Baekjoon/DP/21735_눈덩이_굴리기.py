'''
길이 N인 앞마당에서 M초동안 눈덩이 굴리기
초기 눈덩이 : 1
초시 시작 : 0

1. 눈덩이 위치 += 1 -> 눈덩이 크기 1만큼 늘어남
2. 눈덩이 위치 += 2 -> 눈덩이 크기 // 2 + 2

앞마당 끝에 도달하면 끝
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(M+1)]
dp[0][0] = 1

for i in range(M):
    for j in range(N):

        if dp[i][j] == 0:
            continue

        # 1칸 이동
        if j+1 <= N:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + arr[j])

        # 2칸 이동
        if j+2 <= N:
            dp[i+1][j+2] = max(dp[i+1][j+2], dp[i][j]//2 + arr[j+1])

print(max(max(dp[i]) for i in range(M+1)))