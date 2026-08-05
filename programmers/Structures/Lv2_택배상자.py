'''
보조 컨테이너 구조 : 스택
'''

def solution(order):
    stack = []
    idx = 0

    for box in range(1, len(order) + 1):
        
        if box == order[idx]:
            idx += 1

            while stack and idx < len(order) and stack[-1] == order[idx]:
                stack.pop()
                idx += 1
        else:
            stack.append(box)

    return idx