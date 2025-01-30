string = input()

stack = []
total = 0
temp = 1

print(len(string), string)
for i in range(len(string)):

    cur = string[i]

    if not stack:

        if cur in [')', ']']:
            print(0)
            break

        else:
            stack.append(cur)

    else:
        if cur in ['(', '[']:
            stack.append(cur)

        elif cur == ')' and stack[-1] == '(':
            stack.pop()

        elif cur == ']' and stack[-1] == '[':
            stack.pop()

        else:
            print(0)
            break
