# 다익스트라

from heapq import heappush, heappop

n = int(input())
rooms = [list(input()) for _ in range(n)]
changes = [[float('inf')] * n for _ in range(n)]
changes[0][0] = 0

pq = [(0, 0, 0)]  # 방 바꾼수, r, c

while pq:

    cur_change, cur_r, cur_c = heappop(pq)

    if (cur_r, cur_c) == (n-1, n-1):
        print(cur_change)
        exit(0)

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_r, next_c = cur_r + di, cur_c + dj

        if 0 <= next_r < n and 0 <= next_c < n and changes[next_r][next_c] == float('inf'):

            # 다음 방이 흰 방일 때
            if rooms[next_r][next_c] == "1":
                changes[next_r][next_c] = min(cur_change, changes[next_r][next_c])
                heappush(pq, (cur_change, next_r, next_c))

            # 다음 방이 검은 방일 때
            elif rooms[next_r][next_c] == "0":
                changes[next_r][next_c] = min(cur_change + 1, changes[next_r][next_c])
                heappush(pq, (cur_change + 1, next_r, next_c))