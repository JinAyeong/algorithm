'''
그냥 점프 : 스카이 콩콩의 힘만큼 좌우 점프
힘을 모아 점프 : 스카이 콩콩의 힘의 배수 위치로 점프
'''

from collections import deque

A, B, N, M = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0

q = deque([(0, N)])

while q:
    m, n = q.popleft()

    if n == M:
        print(m)
        break

    for next in [n - 1, n + 1, n + A, n - A, n + B, n - B, n * A, n * B]:

        if 0 <= next < 100001 and visited[next] == -1:
            visited[next] = m + 1
            q.append((m+1, next))