'''
세로N, 가로M
1. if 경계값 T <= 세가지 색상 평균 : 픽셀255 else 0
2. 새로운 화면에서 값이 255라면 물체
3. 값이 255인 물체의 상하좌우 픽셀 : 같은 물체
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
new_mp = [[False] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        R, G, B = mp[i][j*3], mp[i][j*3+1], mp[i][j*3+2]
        pixel = (R + G + B) // 3

        if pixel >= T:
            new_mp[i][j] = True

def find_object(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and new_mp[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

answer = 0

for i in range(N):
    for j in range(M):
        if new_mp[i][j] and not visited[i][j]:
            answer += 1
            find_object(i, j)

print(answer)