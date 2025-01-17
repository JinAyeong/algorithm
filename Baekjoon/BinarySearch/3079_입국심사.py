N, M = map(int, input().split())  # 입국심사대 수, 상근이와 친구들 수
time = [int(input()) for _ in range(N)]

low = min(time)
high = max(time) * M
result = high

while low <= high:

    mid = (low + high) // 2

    people = 0

    for i in range(N):

        people += mid // time[i]

    if people < M:
        low = mid + 1
    else:
        high = mid - 1
        result = mid

print(result)


#-------------------------------------------------------------------
# 실패 코드 : low, high 범위 잘못 설정
N, M = map(int, input().split())  # 입국심사대 수, 상근이와 친구들 수
time = [int(input()) for _ in range(N)]

low = 1
high = 1000000000
result = 0

while low <= high:

    mid = (low + high) // 2

    people = 0

    for i in range(N):

        people += mid // time[i]

    if people < M:
        low = mid + 1
    else:
        high = mid - 1
        result = mid

print(result)