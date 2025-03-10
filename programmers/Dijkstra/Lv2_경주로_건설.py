'''
직선도로 : 다음 칸으로 넘어갈때마다 100원, 코너 : 방향을 꺾을때마다 500원
방향 : (-1, 0), (0, 1), (1, 0), (0, -1) 위, 오, 아래, 왼
'''

from heapq import heappush, heappop


def solution(board):
    answer = 0
    n = len(board)
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    money = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    money[0][0][1] = money[0][0][2] = 0
    heap = []  # 비용, 방향, x, y
    heappush(heap, (0, 1, 0, 0))
    heappush(heap, (0, 2, 0, 0))

    while heap:

        m, d, x, y = heappop(heap)

        if (x, y) == (n - 1, n - 1):
            answer = m
            break

        if money[x][y][d] < m:
            continue

        # 다음 방향 (좌회전, 직선, 우회전)
        for nd in [(d + 3) % 4, d, (d + 1) % 4]:
            nx, ny = x + direction[nd][0], y + direction[nd][1]

            # 다음칸 건설 비용
            if nd == d:
                nm = m + 100
            else:
                nm = m + 600

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and nm < money[nx][ny][nd]:
                money[nx][ny][nd] = nm
                heappush(heap, (nm, nd, nx, ny))

    return answer