from collections import deque

def valid_parentheses(string):
    stack = []

    match = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for ch in string:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack


def solution(s):
    answer = 0
    s = deque(s)

    for _ in range(len(s)):
        if valid_parentheses(s):
            answer += 1
        s.append(s.popleft())

    return answer