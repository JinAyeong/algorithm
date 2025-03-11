N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

low = 1 # ZeroDivisionError 방지
high = max(arr)
result = 0

while low <= high:
    mid = (low + high) // 2

    cnt = 0

    for i in arr:
        cnt += (i // mid)

        if cnt >= K:
            break

    if cnt >= K:
        low = mid + 1
        result = max(result, mid)

    else:
        high = mid - 1

print(result)