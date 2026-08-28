def solution(n, t, m, p):
    answer = ''
    
    def trans(n, num):
        if num == 0:
            return '0'
        
        num_dict = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        
        result = ''
        
        while num > 0:
            result = str(num % n if num % n < 10 else num_dict[num % n]) + result
            num = num // n
            
        return result
    
    num_str = ''
    i = 0
    
    while len(num_str) < t * m:
        num_str += trans(n, i)
        i += 1
    
    for j in range(p - 1, t * m, m):
        answer += num_str[j]
        
        if len(answer) == t:
            break
    
    return answer