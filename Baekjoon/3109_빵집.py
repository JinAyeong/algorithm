R, C = map(int, input().split()) # 세로, 가로
arr = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
result = 0

def pipe(i, j):

    # 열 끝에 도달했으면 1 return
    if j == C-1:
        return 1

    for di, dj in [(-1, 1), (0, 1), (1, 1)]: # 대각선 위, 오른쪽, 대각선 아래 순서로 탐색

        ni, nj = i + di, j + dj

        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != 'x':
            visited[ni][nj] = True
            if pipe(ni, nj): # 끝에 도달했으면 1 return
                return 1

    return 0 # 도달하지 못하고 끝나면 0 return

for d in range(R):
    result += pipe(d, 0)

print(result)