def solution(n):
    
    left = 1
    right = 1
    
    cur_sum = 1
    answer = 0
    
    while right <= n:
        
        if cur_sum == n:
            answer += 1
            right += 1
            cur_sum += right
        
        elif cur_sum < n:
            right += 1
            cur_sum += right
        
        elif cur_sum > n:
            cur_sum -= left
            left += 1
            
    return answer