from collections import deque

A, B = map(int, input().split())
q = deque([(A, 1)])

while q:
    num, cnt = q.popleft()

    if num == B:
        print(cnt)
        break

    for next in [num * 2, num * 10 + 1]:
        if next <= B:
            q.append((next, cnt + 1))
else:
    print(-1)
