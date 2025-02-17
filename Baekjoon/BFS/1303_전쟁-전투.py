from collections import deque

N, M = map(int, input().split()) # 가로, 세로
mp = [list(input()) for _ in range(M)]

white = 0
blue = 0

def bfs(x, y, color):
    cnt = 1
    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < M and 0 <= ny < N and mp[nx][ny] == color:
                mp[nx][ny] = 'X'
                q.append((nx, ny))
                cnt += 1

    return cnt

for i in range(M):
    for j in range(N):
        if mp[i][j] == "W":
            mp[i][j] = "X"
            cur_cnt = bfs(i, j, "W")
            white += cur_cnt ** 2

        elif mp[i][j] == "B":
            mp[i][j] = "X"
            cur_cnt = bfs(i, j, "B")
            blue += cur_cnt ** 2

print(white, blue)