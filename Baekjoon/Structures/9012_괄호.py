for _ in range(int(input())):

    arr = input()
    stack = 0
    answer = 'YES'

    for i in arr:

        if i == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                answer = 'NO'
                break

    if stack:
        answer = 'NO'

    print(answer)