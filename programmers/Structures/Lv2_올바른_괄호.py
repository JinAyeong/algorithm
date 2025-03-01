def solution(s):
    answer = True
    stack = 0
    for char in s:
        if char == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                answer = False
                break
    if stack:
        answer = False

    return answer