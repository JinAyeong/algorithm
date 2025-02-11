# 하루 지날 때 마다 중량 K만큼 감소

N, K = map(int, input().split())
kit = list(map(int, input().split()))
result = 0
used = [False] * N

def dfs(day, weight):
    global result

    if day == N:
        result += 1
        return

    for i in range(N):
        if not used[i] and weight - K + kit[i] >= 500:
            used[i] = True
            dfs(day + 1, weight - K + kit[i])
            used[i] = False

dfs(0, 500)

print(result)