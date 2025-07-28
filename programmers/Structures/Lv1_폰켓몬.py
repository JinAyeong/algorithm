def solution(nums):
    cnt = set(nums)
    answer = min(len(cnt), len(nums) // 2)

    return answer