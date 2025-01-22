N = int(input())

stack = []
result = 0

for _ in range(N):

    i, h = map(int, input().split())

    # 입력의 첫번째 높이가 0일 때 고려 (질문게시판 보고 해결..)
    if not stack and h != 0:
        stack.append(h)

    else:
        while stack:

            if stack[-1] < h:
                stack.append(h)

            elif stack[-1] == h:
                break

            elif stack[-1] > h:
                stack.pop()
                result += 1

        if not stack and h != 0:
            stack.append(h)

result += len(stack)

print(result)