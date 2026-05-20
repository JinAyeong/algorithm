'''
자료구조 : 스택
1: 빵, 2: 야채, 3: 고기
1-2-3-1 순서일때 햄버거 하나
'''

def solution(ingredient):
    answer = 0
    
    stack = []
    
    def can_make_hamburger(stack):
        if len(stack) < 3:
            return False
        if not(stack[-3] == 1 and stack[-2] == 2 and stack[-1] == 3):
            return False
        return True
    
    for i in ingredient:
        if i == 1 and can_make_hamburger(stack):
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1
        else:
            stack.append(i)
    
    return answer