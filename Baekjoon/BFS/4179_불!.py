from collections import deque

R, C = map(int, input().split()) # 세로, 가로
room = [list(input()) for _ in range(R)]
start = (0, 0, 0)
q = deque([])

for a in range(R):
    for b in range(C):
        if room[a][b] == 'J':
            start = ('J', a, b, 0)

        elif room[a][b] == 'F':
            q.append(('F', a, b, 0))

q.append(start)

visited = [[False] * C for _ in range(R)]

result = 'IMPOSSIBLE'

while q:

    type, cr, cc, ct = q.popleft()

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = cr + di, cc + dj

        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and room[nr][nc] == '.':
            visited[nr][nc] = True
            q.append((type, nr, nc, ct + 1))

        elif not (0 <= nr < R and 0 <= nc < C):
            if type == 'J':
                result = ct + 1
                break

    if result != 'IMPOSSIBLE':
        break

print(result)