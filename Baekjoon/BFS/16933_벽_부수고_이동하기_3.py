'''
0: 이동 가능, 1: 이동 불가능
(N, M)까지 최단경로로 이동
벽 K개까지 부수고 이동 가능

- 벽 부순 유무 포함하여 저장
- 이동횟수 짝수 : 낮, 홀수 : 밤
- 이동안하고 머무르기 가능 (방문 += 1)
- 벽은 낮에만 부수기 가능 (벽 부수고 싶은데, 밤일 경우에는 이동 += 2로 이동)
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
mp = [input().strip() for _ in range(N)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]

def solve():
    visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
    
    q = deque()
    q.append((0, 0, 0, 1))
    visited[0][0][0] = True
    
    while q:
        r, c, k, t = q.popleft()
        
        if r == N-1 and c == M-1:
            return t
        
        day = t % 2  # 1: 낮, 0: 밤
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            
            # 빈칸
            if mp[nr][nc] == '0' and not visited[nr][nc][k]:
                    visited[nr][nc][k] = True
                    q.append((nr, nc, k, t+1))
            
            # 벽
            elif k < K and mp[nr][nc] == '1' and not visited[nr][nc][k+1]:
                
                # 낮
                if day:
                    visited[nr][nc][k+1] = True
                    q.append((nr, nc, k+1, t+1))
                
                # 밤
                else:
                    q.append((r, c, k, t+1))
    
    return -1

print(solve())