from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
    visited = [[[False] * m for _ in range(n)] for _ in range(4)]
    
    # 시작/끝 지점 탐색
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                si, sj = i, j
            elif board[i][j] == 'G':
                ei, ej = i, j
                
    q = deque([(si, sj, k, 0) for k in range(4)])
    
    # 상하좌우 이동
    def move(mp, i, j, d):
        
        while True:
            
            di, dj = dir[d][0], dir[d][1]
            ni, nj = i + di, j + dj
                
            if 0 <= ni < n and 0 <= nj < m and mp[ni][nj] != 'D':
                i, j = ni, nj
                
            else:
                return i, j
    
    while q:
        i, j, d, t = q.popleft()
        if (i, j) == (ei, ej):
            return t
        
        for nd in range(4):
            ni, nj = move(board, i, j, d)
            if not visited[nd][ni][nj]:
                visited[nd][ni][nj] = True
                q.append((ni, nj, nd, t+1))
    
    return -1