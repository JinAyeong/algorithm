import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr[a] = a+1 일에 잡혀있는 상담과 보수

dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):

    # 상담을 안하는 경우
    dp[i] = dp[i+1]

    t, p = arr[i]

    # 상담을 하는 경우
    if i + t <= N:
        dp[i] = max(dp[i], dp[i+t] + p)

print(dp[0])