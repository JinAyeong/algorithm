from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def search(idx, ci, cj):

            if idx == len(word):
                return True

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == word[idx]:
                    visited[ni][nj] = True
                    if search(idx+1, ni, nj):
                        return True
                    visited[ni][nj] = False

            return False


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = [[False] * m for _ in range(n)]
                    visited[i][j] = True

                    if search(1, i, j):
                        return True

        return False