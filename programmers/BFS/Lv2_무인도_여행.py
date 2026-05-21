'''
상하좌우로 연결된 칸에 적힌 숫자의 합 = 무인도에서 머물 수 있는 수
각 섬에서 머물 수 있는 최대 수 배열 리턴
'''
from collections import deque

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(i, j):
        
        visited[i][j] = True        
        q = deque([(i, j)])
        day = int(maps[i][j])
        
        while q:
            ci, cj = q.popleft()
            
            for di, dj in dir:
                ni, nj = ci + di, cj + dj
                
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 'X' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    day += int(maps[ni][nj])
                    q.append((ni, nj))
                    
        return day
            
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] or maps[i][j] == 'X':
                visited[i][j] = True
                continue
            answer.append(bfs(i, j))
    
    if not answer:
        answer.append(-1)
        
    answer.sort()
    
    return answer