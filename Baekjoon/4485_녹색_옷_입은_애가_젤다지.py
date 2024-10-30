from heapq import heappush, heappop

cnt = 0

while True:
    N = int(input())
    cnt += 1

    if N == 0:
        exit(0)

    game = [list(map(int, input().split())) for _ in range(N)]

    money = [[float('inf')] * N for _ in range(N)]
    money[0][0] = game[0][0]

    pq = [(game[0][0], 0, 0)]  # money, r, c

    while pq:

        cur_m, r, c = heappop(pq)
        if (r, c) == (N-1, N-1):
            print(f'Problem {cnt}: {cur_m}')
            break

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + di, c + dj

            if 0 <= nr < N and 0 <= nc < N and cur_m + game[nr][nc] < money[nr][nc]:
                money[nr][nc] = cur_m + game[nr][nc]
                heappush(pq, (cur_m + game[nr][nc], nr, nc))