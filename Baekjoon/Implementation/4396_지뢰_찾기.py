N = int(input())
mp = [list(input()) for _ in range(N)]
open_mp = [list(input()) for _ in range(N)]

def search(x, y):

    result = 0

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:

            if mp[nx][ny] == '*':
                result += 1

    return result

def stepped():

    for x in range(N):
        for y in range(N):
            if mp[x][y] == "*":
                open_mp[x][y] = "*"


step = False

for i in range(N):
    for j in range(N):
        if open_mp[i][j] == 'x':
            if mp[i][j] == '*':
                step = True
            else:
                open_mp[i][j] = str(search(i, j))

if step:
    stepped()

for line in open_mp:
    print(''.join(line))