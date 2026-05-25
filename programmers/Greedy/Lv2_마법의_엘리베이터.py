def solution(storey):
    answer = 0
    nums = [0] + list(map(int, str(storey)))

    for i in range(len(nums)-1, 0, -1):
        cur = nums[i]

        if cur > 5:
            answer += 10 - cur
            nums[i-1] += 1

        elif cur < 5:
            answer += cur

        elif cur == 5:
            if nums[i-1] >= 5:
                answer += 5
                nums[i-1] += 1
            else:
                answer += 5

    answer += nums[0]

    return answer