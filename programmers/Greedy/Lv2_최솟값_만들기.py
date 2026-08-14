def solution(A,B):
    answer = 0
    n = len(A)
    
    A.sort()
    B.sort()
    
    for i in range(n):
        answer += A[i] * B[n-i-1]

    return answer