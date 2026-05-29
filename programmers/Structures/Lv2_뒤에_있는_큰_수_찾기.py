def solution(numbers):
    
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        
        cur = numbers[i]
        
        while stack:
            
            if cur >= stack[-1]:
                stack.pop()
            else:
                break
                
        if stack:
            answer[i] = stack[-1]
            
        stack.append(cur)
    
    return answer