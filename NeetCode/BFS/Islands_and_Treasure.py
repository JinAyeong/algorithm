from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n, m = len(grid), len(grid[0])

        q = deque((0, i, j) for i in range(n) for j in range(m) if grid[i][j] == 0)

        while q:

            cd, ci, cj = q.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 2147483647 and grid[ni][nj] != -1:
                    grid[ni][nj] = min(grid[ni][nj], cd + 1)
                    q.append((cd + 1, ni, nj))