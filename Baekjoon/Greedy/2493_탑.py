N = int(input())
tops = list(map(int, input().split()))

stack = []

for i in range(N):

    # 스택이 비어있다면 : 내 앞에 탑 없음, 0 출력
    if not stack:
        stack.append((tops[i], i))
        print(0, end=' ')

    # 스택에 있다면
    elif stack:

        # 스택이 빌때까지 나보다 작은 탑 제거
        while stack:

            if stack[-1][0] < tops[i]:
                stack.pop()

            # 나보다 큰 탑이 나오면 그 탑 인덱스 출력
            # 내 뒤의 탑 검사를 위해 나도 append 후 break
            else:
                print(stack[-1][1] + 1, end=' ')
                stack.append((tops[i], i))
                break

        # 스택 안에 나보다 작은 탑밖에 없어서 다 pop 했으면 0 출력
        if not stack:
            stack.append((tops[i], i))
            print(0, end=' ')