'''
- n줄, n칸
- 손상된 칸으로 이동 불가능, 이미 지나온 길은 손상된 빙판을 바뀜
- 시작(r1, c1)에서 탈출구(r2, c2)로 이동가능한지 판별
- 탈출구는 빙판 밑에 있음 -> 두번 밟아야 탈출 가능
'''

from collections import deque

n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]

r1, c1 = map(lambda x: int(x) - 1, input().split())
r2, c2 = map(lambda x: int(x) - 1, input().split())

visited = [[False] * m for _ in range(n)]
visited[r1][c1] = True

q = deque([(r1, c1)])

def solve():
    
    while q:
        cr, cc = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < n and 0 <= nc < m:

                # 도착
                if (nr, nc) == (r2, c2):
                    if mp[r2][c2] == 'X':
                        return 'YES'
                    else:
                        for dr2, dc2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr2, nc2 = r2 + dr2, c2 + dc2
                            if 0 <= nr2 < n and 0 <= nc2 < m and mp[nr2][nc2] == '.' and not visited[nr2][nc2]:
                                return 'YES'
                        continue
                
                # 진행
                if mp[nr][nc] == '.' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    return 'NO'

print(solve())