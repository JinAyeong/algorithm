import sys
sys.setrecursionlimit(10**6)

def solution(n):
    
    memo = [0] * (n + 1)
    memo[1] = 1
    
    def fibo(num):
        if num <= 1:
            return memo[num]
        
        if memo[num] == 0:
            memo[num] = (fibo(num-1) + fibo(num-2)) % 1234567
        
        return memo[num]
    
    return fibo(n)