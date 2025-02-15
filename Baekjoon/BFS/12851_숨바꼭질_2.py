from collections import deque

N, K = map(int, input().split())
q = deque([(0, N)])
visited = [-1] * 100001
visited[N] = 0
result = float('inf')
cnt = 0

while q:
    t, c = q.popleft()

    # 수빈이를 찾았을 경우
    if c == K:
        # 처음 찾았으면 t가 최소 시간 -> 결과와 cnt 갱신
        if result == float('inf'):
            result = t
            cnt = 1

        # 결과와 같은 시간으로 도착했을 경우 -> cnt += 1
        elif result == t:
            cnt += 1

    # t가 이미 결과보다 오래 걸렸을 경우 -> continue
    if t >= result:
        continue

    # 다음 이동 경우의 수 세가지 순회
    for next in [c-1, c+1, c*2]:
        if 0 <= next < 100001:
            # 만약 처음 오는 곳이거나, 이미 가장 빠르게 갈 수 있는 시간과 같은 시간으로 도달할 경우
            # deque에 추가, 처음 오는 곳일 경우 visited 갱신
            if visited[next] == -1 or visited[next] == t+1:
                visited[next] = t+1
                q.append((t+1, next))

print(result)
print(cnt)