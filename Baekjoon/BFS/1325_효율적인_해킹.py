import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[b].append(a)

max_cnt = 0
max_numbers = []

def bfs(n):

    visited = [False] * (N+1)
    visited[n] = True
    q = deque([n])
    cnt = 1

    while q:
        cur = q.popleft()

        for next in adjl[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1

    return cnt

for i in range(1, N+1):

    cur_cnt = bfs(i)

    if cur_cnt > max_cnt:
        max_cnt = cur_cnt
        max_numbers = [i]

    elif cur_cnt == max_cnt:
        max_numbers.append(i)

print(*max_numbers)