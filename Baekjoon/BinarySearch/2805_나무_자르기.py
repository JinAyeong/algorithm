import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
result = 0

while low <= high:

    mid = (low + high) // 2

    cur_length = 0

    for tree in trees:
        if mid < tree:
            cur_length += (tree - mid)

    if cur_length >= M:
        low = mid + 1
        result = mid
        if cur_length == M:
            break

    else:
        high = mid - 1

print(result)