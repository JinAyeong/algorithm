'''
1. 실행 대기 큐에서 대기중인 프로세스 하나 pop
2. 우선순위가 더 높은 프로세스가 있으면 다시 push
3. 없으면 방금 pop한 프로세스 실행
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    
    n = len(priorities)
    priorities = deque(priorities)
    idx = deque(range(n))
    
    while priorities:
        cur = priorities.popleft()
        cur_idx = idx.popleft()
        
        if priorities and max(priorities) > cur:
            priorities.append(cur)
            idx.append(cur_idx)
        else:
            answer += 1
            
            if cur_idx == location:
                break
    
    return answer