tc = 0

while True:
    tc += 1
    string = input()
    answer = 0

    if '-' in string:
        break

    stack = []

    for c in string:
        if c == '{':
            stack.append(c)
        else:
            if not stack:
                answer += 1
                stack.append('{')
            elif stack[-1] == '{':
                stack.pop()

    if stack:
        answer += len(stack) // 2

    print(f'{tc}. {answer}')