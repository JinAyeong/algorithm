from collections import Counter

def solution(topping):
    answer = 0
    n = len(topping)
    
    left = Counter(topping)
    right = set()
    
    for t in topping:
        
        # 오른쪽에 토핑 추가
        right.add(t)
        
        # 왼쪽에 토핑 삭제
        if left[t] == 1:
            del left[t]
        else:
            left[t] -= 1
            
        # 토핑 검사
        if len(left) == len(right):
            answer += 1
    
    return answer