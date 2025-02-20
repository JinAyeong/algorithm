N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)
result = float('inf')

while left <= right:

    mid = (left + right) // 2
    cnt = 1
    cur = 0

    for i in arr:
        if cur + i > mid:
            cnt += 1
            cur = 0
        cur += i


    if cnt <= M:
        result = min(mid, result)
        right = mid - 1

    elif cnt > M:
        left = mid + 1

print(result)