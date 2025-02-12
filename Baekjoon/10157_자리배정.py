C, R = map(int, input().split()) # 가로, 세로
number = int(input())

if C * R < number:
    print(0)
    exit(0)

seat = [[0] * C for _ in range(R)]

cur = 1
i, j = R-1, 0

d = 0
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while cur <= C * R:

    seat[i][j] = cur
    if cur == number:
        print(i+1, j+1)
        break
    cur += 1

    ni, nj = i + dir[d][0], j + dir[d][1]

    if not (0 <= ni < R and 0 <= nj < C and seat[ni][nj] == 0):
        d = (d + 1) % 4
        ni, nj = i + dir[d][0], j + dir[d][1]

    i, j = ni, nj