# deque : 모든 가중치가 동일할때
# heap : 가중치가 다를때
# visited 배열 관리 방식: 좌표를 먼저 관리하고 말처럼 이동한 횟수는 나중에 처리하는 구조가 더 효율적
# -> [r][c][k+1] O , [k+1][r][c] X
# True/False 사용: Python의 부울형 처리가 더 빠름
# deque에 담는 값의 구조: 좌표 정보를 먼저 처리하는 것이 성능 좋음

from collections import deque

K = int(input())
W, H = map(int, input().split())  # 가로 세로
board = [list(map(int, input().split())) for _ in range(H)]

horse = [
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2)
]

monkey = [(-1, 0), (1, 0), (0, 1), (0, -1)]

q = deque([(0, 0, 0, 0)])  # 이동횟수, k횟수, 현재위치 r, c
visited = [[[0] * W for _ in range(H)] for _ in range(K+1)]

while q:

    move, k, r, c = q.popleft()

    if (r, c) == (H-1, W-1):
        print(move)
        exit(0)

    # 말 이동
    if k < K:
        for di, dj in horse:
            hr, hc = r + di, c + dj

            if 0 <= hr < H and 0 <= hc < W and not board[hr][hc] and not visited[k+1][hr][hc]:
                visited[k+1][hr][hc] = 1
                q.append((move+1, k+1, hr, hc))


    # 원숭이 이동
    for di, dj in monkey:
        mr, mc = r + di, c + dj

        if 0 <= mr < H and 0 <= mc < W and not board[mr][mc] and not visited[k][mr][mc]:
            visited[k][mr][mc] = 1
            q.append((move + 1, k, mr, mc))

print(-1)