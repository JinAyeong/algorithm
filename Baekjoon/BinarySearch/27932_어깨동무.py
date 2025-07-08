'''
지친사람의 수 최댓값 k
점수차가 h일 경우, 옆사람과의 키차이가 h이하이면 지치지 않음
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

low = 0
high = max(arr)
answer = 0

while low <= high:
    mid = (low + high) // 2

    cnt = 0

    for i in range(n):
        left = (arr[i-1] if i > 0 else arr[i])
        right = (arr[i+1] if i < n - 1 else arr[i])

        if abs(left - arr[i]) > mid or abs(right - arr[i]) > mid:
            cnt += 1

    if cnt <= k:
        high = mid - 1
        answer = mid

    else:
        low = mid + 1

print(answer)