C, R = map(int, input().split()) # 가로, 세로
number = int(input())

if C * R < number:
    print(0)
    exit(0)

# 좌석 오른쪽으로 90도 회전 - 가로 세로 변경
seat = [[0] * R for _ in range(C)]

cur = 1
i, j = 0, 0

d = 0
# 좌석 오른쪽으로 90도 회전 - 오 위 왼 아
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while cur <= C * R:

    seat[i][j] = cur

    # 좌석 배정 했으면 프린트 후 브레이크
    if cur == number:
        print(i+1, j+1)
        break

    cur += 1

    ni, nj = i + dir[d][0], j + dir[d][1]

    if not (0 <= ni < C and 0 <= nj < R and seat[ni][nj] == 0):
        d = (d + 1) % 4
        ni, nj = i + dir[d][0], j + dir[d][1]

    i, j = ni, nj