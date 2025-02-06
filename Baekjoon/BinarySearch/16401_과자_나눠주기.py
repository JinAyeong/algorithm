import sys
input = sys.stdin.readline

M, N = map(int, input().split()) # 조카 수, 과자 수
snacks = list(map(int, input().split()))
left = 1
right = 1000000000

result = 0

while left <= right:

    length = (left + right) // 2

    cnt = 0

    for snack in snacks:
        cnt += snack // length

        if cnt >= M:
            break

    if cnt >= M:
        left = length + 1
        result = length
    else:
        right = length - 1

print(result)