string = input()

stack = []
total = 0
temp = 1
open = {'(':2, '[':3}
close = {')':2, ']':3}

for i in range(len(string)):

    cur = string[i]

    if cur in open:
        stack.append(cur)
        temp *= open[cur]

    elif cur in close:
        if not stack:
            total = 0
            break

        elif stack[-1] in open and open[stack[-1]] != close[cur]:
            total = 0
            break

        elif stack[-1] in open and string[i-1] == stack[-1]:
            total += temp

        stack.pop()
        temp //= close[cur]

if stack:
    total = 0

print(total)