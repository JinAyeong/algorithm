def solution(number, k):
    answer = ''
    n = len(number)
    stack = []
    deleted = 0
    
    for num in number:
        num = int(num)
        
        while True:
            if not stack:
                stack.append(num)
                break
            elif stack[-1] < num and deleted < k:
                stack.pop()
                deleted += 1
            else:
                stack.append(num)
                break
                
    if len(stack) > n-k:
        while not(len(stack) == n-k):
            stack.pop()
                
    answer = "".join(list(map(str, stack)))
    
    return answer