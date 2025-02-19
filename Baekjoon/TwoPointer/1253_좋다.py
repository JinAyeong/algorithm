N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = 0

for i in range(N):
    cur = numbers[i]
    left = 0
    right = N - 1

    while left < right:

        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue

        cur_sum = numbers[left] + numbers[right]

        if cur_sum == cur:
            result += 1
            break

        elif cur_sum < cur:
            left += 1

        elif cur_sum > cur:
            right -= 1

print(result)