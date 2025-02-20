N = int(input())
arr = list(map(int, input().split()))
M = int(input())

left = 0
right = max(arr)
result = 0

while left <= right:

    mid = (left + right) // 2
    cur_sum = 0

    for num in arr:
        cur_sum += min(num, mid)

    if cur_sum <= M:
        result = max(result, mid)
        left = mid + 1

    else:
        right = mid - 1

print(result)