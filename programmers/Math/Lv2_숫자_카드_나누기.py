'''
A, B의 최대공약수 찾기
'''
import math

def solution(arrayA, arrayB):
    
    gcd_a = math.gcd(*arrayA)
    gcd_b = math.gcd(*arrayB)
    
    gcd_a = (0 if any(b % gcd_a == 0 for b in arrayB) else gcd_a)
    gcd_b = (0 if any(a % gcd_b == 0 for a in arrayA) else gcd_b)
    
    answer = max(gcd_a, gcd_b)
    
    return answer