# 성공 코드 : 이동 노드 while 문으로 부모 추적

from collections import deque

N, K = map(int, input().split())

q = deque([(0, N)])
visited = [-1] * 100001
visited[N] = True
visited[N] = N

while q:

    ct, cc = q.popleft()

    if cc == K:
        print(ct)
        break

    for nc in [cc-1, cc+1, cc*2]:
        if 0 <= nc < 100001 and visited[nc] == -1:
            visited[nc] = cc
            q.append((ct+1, nc))

result = []
cur = K
while cur != N:
    result.append(cur)
    cur = visited[cur]
result.append(N)

print(*result[::-1])


#---------------------------------------------------
# 실패 코드 1 : 이동 노드 dfs 탐색
import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

q = deque([(0, N)])
visited = [-1] * 100001
visited[N] = True
visited[N] = N


def parent(n, lst):
    if n == N:
        return lst

    result = parent(visited[n], [visited[n]] + lst)

    if result:
        return result

while q:

    ct, cc = q.popleft()

    if cc == K:
        print(ct)
        print(*parent(K, [K]))
        break

    for nc in [cc-1, cc+1, cc*2]:
        if 0 <= nc < 100001 and visited[nc] == -1:
            visited[nc] = cc
            q.append((ct+1, nc))


#---------------------------------------------------
# 실패 코드 2 : 이동 경로 q에 함꼐 저장하여 시간 초과

from collections import deque

N, K = map(int, input().split())

q = deque([(0, N, [N])])
visited = [False] * 100001
visited[N] = True

while q:

    ct, cc, c_lst = q.popleft()

    if cc == K:
        print(ct)
        print(*c_lst)
        break

    for nc in [cc-1, cc+1, cc*2]:
        if 0 <= nc < 100001 and not visited[nc]:
            visited[nc] = True
            q.append((ct+1, nc, c_lst + [nc]))