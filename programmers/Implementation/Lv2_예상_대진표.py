'''
12345678
11223344 : +1 후 2로 나눴을때 몫이 같아질때까지 계속
'''

def solution(n,a,b):
    answer = 0

    while True:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1
        if a == b:
            break

    return answer