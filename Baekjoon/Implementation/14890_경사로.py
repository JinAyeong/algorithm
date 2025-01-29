N, L = map(int, input().rstrip().split())
road = [list(map(int, input().rstrip().split())) for _ in range(N)]

def check(arr):

    cur = arr[0]
    used = [False] * N # 경사로 설치 유무

    for i in range(1, N):
        if arr[i] != cur:

            if abs(arr[i] - cur) > 1:
                return 0

            # 오르막 경사로 설치
            if arr[i] > cur:

                for j in range(i - L, i):
                    if not (0 <= j < N):
                        return 0

                    if arr[j] != cur:
                        return 0

                    if used[j]:
                        return 0

                    used[j] = True

            # 내리막 경사로 설치
            elif arr[i] < cur:

                for j in range(i, i + L):
                    if not (0 <= j < N):
                        return 0

                    if arr[j] != arr[i]:
                        return 0

                    if used[j]:
                        return 0

                    used[j] = True

            cur = arr[i]

    return 1

result = 0

for a in range(N):
    column = [road[b][a] for b in range(N)]

    result += check(road[a])
    result += check(column)

print(result)