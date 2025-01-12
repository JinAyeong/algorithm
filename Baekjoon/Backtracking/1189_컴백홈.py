R, C, K = map(int, input().split()) # 세로, 가로, 거리
arr = [list(input()) for _ in range(R)]

# 한수 : (R-1, 0), 집 : (0, C-1)
# 한번 방문한 곳 재방문 X
# K보다 크면 return

visited = [[False] * C for _ in range(R)]
visited[R-1][0] = True
result = 0

def move(r, c, k):
    global result, R, C, K, visited

    if (r, c) == (0, C-1) and k == K:
        result += 1
        return

    if k > K:
        return

    for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        nr, nc = r + di, c + dj

        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != 'T':
            visited[nr][nc] = True
            move(nr, nc, k+1)
            visited[nr][nc] = False


move(R-1, 0, 1)

print(result)