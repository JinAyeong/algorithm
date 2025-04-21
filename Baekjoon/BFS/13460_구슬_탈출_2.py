'''
1. 보드 상하좌우로 욺직여서 구슬 이동
2, 빨간구슬만 빼내기
3. 각 단계마다 네방향으로 기울이며 두 구슬을 동시에 이동
3-1. 파란구슬이 구멍에 빠지면 실패
3-2. 빨간구슬이 구멍에 빠지면 성공
3-3. 두 구슬이 같은 위치에 있으면 더 많이 이동한 쪽을 한 칸 뒤로 이동 (중요!)
4. 10회 반복 후, 성공 못하면 -1
'''

from collections import deque

# 구슬 굴리기
def move(x, y, dx, dy, board):
    cnt = 0 # 이동 거리

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1

    return x, y, cnt

# 구슬 탐색
def bfs(board, rx, ry, bx, by):
    visited = [[[[False] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    visited[rx][ry][bx][by] = True

    q = deque([(rx, ry, bx, by, 0)])

    while q:
        rx, ry, bx, by, depth = q.popleft()

        # 10번 넘게 기울이면 실패
        if depth >= 10:
            return -1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            nrx, nry, rc = move(rx, ry, dx, dy, board)
            nbx, nby, bc = move(bx, by, dx, dy, board)

            # 파란 구슬이 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 구슬이 같은 위치에 있으면, 더 많이 이동한 구슬을 한 칸 뒤로
            if (nrx, nry) == (nbx, nby):
                if rc > bc:
                    nrx -= dx
                    nry -= dy

                else:
                    nbx -= dx
                    nby -= dy

            # 아직 방문하지 않은 상태이면 큐에 추가
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

print(bfs(board, rx, ry, bx, by))