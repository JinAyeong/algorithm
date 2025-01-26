# dp

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * n for _ in range(n)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):

        if (i, j) == (0, 0):
            continue

        if 0 <= i-1 < n:
            up = dp[i-1][j] + max(0, arr[i][j] - arr[i-1][j] + 1)
        else:
            up = float('inf')

        if 0 <= j-1 < n:
            left = dp[i][j-1] + max(0, arr[i][j] - arr[i][j-1] + 1)
        else:
            left = float('inf')

        dp[i][j] = min(up, left)

print(dp[n-1][n-1])

#---------------------------------------------------------------------
# 다익스트라 - 시간초과

from heapq import heappop, heappush

# 1. A[a][b] > A[c][d]
# 2. 1 <= i, j < n : A[i][j+1] , A[i+1][j]
# 3. 1 <= i < n , j ==n : A[i][j+1]
# 4. 1 == n, 1 <= j < n : A[i+1][j]
# 버튼 누르면 1원의 비용

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[float('inf')] * n for _ in range(n)]
visited[0][0] = 0
heap = [(0, 0, 0)]

while heap:

    button, r, c = heappop(heap)

    if (r, c) == (n-1, n-1):
        print(button)
        break

    if button > visited[r][c]:
        continue

    for di, dj in [(1, 0), (0, 1)]:
        nr, nc = r + di, c + dj

        if not (0 <= nr < n and 0 <= nc < n):
            continue

        if arr[r][c] > arr[nr][nc]:
            next_button = button

        else:
            next_button = button + (arr[nr][nc] - arr[r][c]) + 1

        if next_button < visited[nr][nc]:
            visited[nr][nc] = next_button
            heappush(heap, (next_button, nr, nc))