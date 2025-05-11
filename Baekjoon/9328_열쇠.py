'''
' : 빈공간, * : 벽, $ : 훔칠문서, 알파벳 소문자 : 열쇠, 알파벳 대문자 : 문
1. 맵 너비우선 탐색
2. 문을 만날 경우 열쇠 있는지 확인
3. 열쇠가 없으면 열쇠 찾을 때 까지 보류
4. 열쇠가 있으면 계속 너비우선 탐색
'''

from collections import deque

for tc in range(int(input())):

    h, w = map(int, input().split())

    mp = [list(input()) for _ in range(h)]

    key = input()
    if key == '0':
        key = []
    else:
        key = set(key)

    start = (-1, -1)

    # 빌딩 가장자리 탐색
    for i in range(h):
        if start != (-1, -1):
            break
        for j in range(w):
            if 1 <= i < h-1 and 1 <= j < w-1:
                continue
            if mp[i][j] == '.':
                start = (i, j)
                break

    if start == (-1, -1):
        print(0)
        continue

    q = deque([start])
    visited = [[False] * w for _ in range(h)]
    alphabet = {}
    cnt = 0

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and mp[ni][nj] != '*':
                visited[ni][nj] = True
                if mp[ni][nj] == '.':
                    q.append((ni, nj))
                else:
                    