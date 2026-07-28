'''
1. n*n 2차원 배열 생성
2. 1행 1열부터 i행 i열의 내용을 숫자 i로 채움
3. n*n 평탄화 -> 1차원 배열 arr 생성
4. arr[left], arr[left+1], ... , arr[right]만 남기고 나머지 삭제

0123456789
1234223433
'''

def solution(n, left, right):
    answer = [0] * (right - left + 1)
    
    for i in range(right - left + 1):
        
        num = i+left
        value = max((num//n)+1, (num%n)+1)
        answer[i] = value
        
    return answer