import sys
input = sys.stdin.readline
from collections import deque

puzzle = [list(map(int, input().split())) for _ in range(3)]
blank = next((i, j) for i in range(3) for j in range(3) if puzzle[i][j] == 0)
q = deque([(0, blank, puzzle)])
visited = set()

while q:

    cur_move, cur_blank, cur_puzzle = q.popleft()

    if cur_puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        print(cur_move)
        exit(0)

    i, j = cur_blank

    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < 3 and 0 <= nj < 3:
            next_puzzle = [row[:] for row in cur_puzzle]
            next_puzzle[ni][nj], next_puzzle[i][j] = next_puzzle[i][j], next_puzzle[ni][nj]

            if str(next_puzzle) not in visited:
                visited.add(str(next_puzzle))
                q.append((cur_move + 1, (ni, nj), next_puzzle))

print(-1)