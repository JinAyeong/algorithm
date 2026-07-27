from math import ceil, floor

def solution(r1, r2):
    answer = 0
    
    '''
    r1**2 - x**2 <= y**2 <= r2**2 - x**2
    '''

    for x in range(1, r2 + 1):
        
        low = ceil((max(r1**2 - x**2, 0)) ** 0.5)
        high = floor((r2**2 - x**2) ** 0.5)

        answer += (floor(high) - ceil(low) + 1)

    return answer * 4