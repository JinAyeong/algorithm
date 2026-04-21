from collections import deque

def solution(maps):
    
    
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
                
    def bfs(start, end, n, m, maps):
        
        visited = [[False] * m for _ in range(n)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        si, sj = start
        ei, ej = end
        visited[si][sj] = True
        
        q = deque([(si, sj, 0)])
        
        while q:
            ci, cj, ct = q.popleft()
            if (ci, cj) == (ei, ej):
                return ct
            
            for di, dj in dir:
                ni, nj = ci + di, cj + dj
                
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and maps[ni][nj] != 'X':
                    visited[ni][nj] = True
                    q.append((ni, nj, ct + 1))
                    
        return float('inf')
    
    min_t = bfs(S, L, n, m, maps) + bfs(L, E, n, m, maps)
    answer = (min_t if min_t != float('inf') else -1)
    
    return answer