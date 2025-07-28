from collections import Counter


def solution(nums):
    cnt = Counter(nums)

    answer = min(len(cnt), len(nums) // 2)

    return answer