def solution(A, B):
    answer = 0
    
    n = len(A)
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    idx = 0
    
    for a in A:
        b = B[idx]
        if a < b:
            answer += 1
            idx += 1

        if idx == n:
            break
    
    return answer