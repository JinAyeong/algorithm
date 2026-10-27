'''
야근 피로도 = (남은 일의 작업량)^2
'''

# dfs : 리커전에러
def solution(n, works):
    answer = float('inf')
    length = len(works)
    
    # 현재 인덱스, 현재 n, 현재 야근지수
    def dfs(i, cur_n, cur_sum):
        nonlocal answer, length
        
        if i == length:
            answer = min(cur_sum, answer)
            return
        
        if cur_n < 0:
            return
        
        for j in range(min(cur_n + 1, works[i] + 1)):
            dfs(i+1, cur_n - j, cur_sum + (works[i] - j)**2)
            
    dfs(0, n, 0)
    
    return answer


# greedy
'''
야근 피로도 = (남은 일의 작업량)^2
dfs로 각 work 마다 얼만큼 일할지 정하기
'''

from heapq import heappop, heappush, heapify

def solution(n, works):
    
    works = [-w for w in works]
    heapify(works)
    
    for _ in range(n):
        
        work = -heappop(works)
        
        if work == 0:
            break
        
        heappush(works, -(work-1))
    
    answer = sum(work**2 for work in works)
    
    return answer