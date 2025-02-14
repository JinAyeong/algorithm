from collections import deque # 가중치가 같으므로 deque

N, K = map(int, input().split())
q = deque([(0, N)])
visited = [-1] * 100001
visited[N] = 0
result = 100001
cnt = 0

while q:
    t, c = q.popleft()

    if c == K and t < result:
        result = t
        cnt = 1

    elif c == K and t == result:
        cnt += 1

    if t >= result:
        continue

    for next in [c-1, c+1, c*2]:
        if 0 <= next < 100001:
            if visited[next] == -1 or visited[next] == t+1:
                visited[next] = t+1
                q.append((t+1, next))

print(result)
print(cnt)