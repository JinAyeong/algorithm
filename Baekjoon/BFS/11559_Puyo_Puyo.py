from collections import deque

mp = [list(input()) for _ in range(12)]

# 뿌요 내리기
def drop():
    for j in range(6):
        q = deque([])

        for i in range(11, -1, -1):
            if mp[i][j] != '.':
                q.append(mp[i][j])

        for i in range(11, -1, -1):
            if q:
                mp[i][j] = q.popleft()
            else:
                mp[i][j] = '.'

# 폭발 처리
def play():
    bomb = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if not visited[i][j] and mp[i][j] != '.':
                q = deque([(i, j)])
                color = mp[i][j]
                visited[i][j] = True
                positions = [(i, j)]
                cnt = 1

                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < 12 and 0 <= nj < 6 and not visited[ni][nj] and mp[ni][nj] == color:
                            visited[ni][nj] = True
                            q.append((ni, nj))
                            positions.append((ni, nj))
                            cnt += 1

                if cnt >= 4:
                    bomb = True
                    for x, y in positions:
                        mp[x][y] = '.'

    if bomb:
        drop()
    return bomb

result = 0
while play():
    result += 1

print(result)
