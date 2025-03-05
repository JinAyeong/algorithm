'''
2변 이상이 닿으면 녹아 없어짐
치즈 모두 녹는데 걸리는 시간 구하기
1. 치즈 배열 만들기
2. 먼저 공기 닿은 부분 먼저 탐색
3. 그 후로 치즈 배열 반복하면서 녹이기
'''

from collections import deque

N, M = map(int, input().split()) # 세로, 가로
mp = [list(map(int, input().split())) for _ in range(N)]

# 외부 공기에 닿은 치즈 녹이기
def outside():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    mp[0][0] = -1
    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()

        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and mp[ni][nj] != 1:
                mp[ni][nj] = -1
                q.append((ni, nj))
                visited[ni][nj] = True

def melting():

    melting_cheese = []

    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                cnt = 0

                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < N and 0 <= nj < M and mp[ni][nj] == -1:
                        cnt += 1

                if cnt >= 2:
                    melting_cheese.append((i, j))

    if not melting_cheese:
        return False

    for x, y in melting_cheese:
        mp[x][y] = 0

    return True

result = 0

while True:
    outside()
    if not melting():
        break
    result += 1

print(result)


#--------------------------------------------------------------------------------------
# 최적화 전
from collections import deque

N, M = map(int, input().split()) # 세로, 가로
mp = [list(map(int, input().split())) for _ in range(N)]
result = 0
all_melt = False

# 외부 공기에 닿은 치즈 녹이기
while not all_melt:
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = -1

    while q:
        i, j = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and mp[ni][nj] == 0:
                visited[ni][nj] = -1
                q.append((ni, nj))
            elif 0 <= ni < N and 0 <= nj < M and mp[ni][nj] == 1:
                visited[ni][nj] += 1

    melted = False

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                mp[i][j] = 0
                melted = True

    if not melted:
        all_melt = True

    else:
        result += 1

print(result)
