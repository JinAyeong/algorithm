import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
mp = [0] + [int(input(), 2) for _ in range(N)]
A, B = map(int, input().split())

visited = [False] * (N+1)
visited[A] = True
q = deque([(A, [A])])

while q:
    cur, cur_route = q.popleft()

    if cur == B:
        print(*cur_route)
        exit(0)

    for i in range(1, N+1):

        hamming_route = mp[i] ^ mp[cur]

        if not visited[i] and bin(hamming_route).count('1') == 1:
            visited[i] = True
            q.append((i, cur_route + [i]))

print(-1)