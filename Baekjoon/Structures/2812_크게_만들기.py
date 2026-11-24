N, K = map(int, input().split())
num = str(input())
stack = []
deleted = 0

for n in num:
    cur = int(n)
    if not stack:
        stack.append(cur)
    else:
        if deleted < K:
            while stack and stack[-1] < cur and deleted < K:
                stack.pop()
                deleted += 1
            stack.append(cur)
        else:
            stack.append(cur)

if deleted < K:
    for _ in range(K-deleted):
        stack.pop()

# for s in stack:
#     print(s, end="")

stack = list(map(str, stack))
print("".join(stack))