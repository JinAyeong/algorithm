def solution(sequence, k):
    
    n = len(sequence)
    left = 0
    cur_sum = 0
    min_len = float('inf')
    answer = [0, 0]

    for right in range(n):
        cur_sum += sequence[right]

        while cur_sum >= k:
            if cur_sum == k:
                if right - left < min_len:
                    min_len = right - left
                    answer = [left, right]

            cur_sum -= sequence[left]
            left += 1

    return answer