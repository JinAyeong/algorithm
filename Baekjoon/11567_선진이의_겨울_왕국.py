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

q = deque([(r1, c1)])
mp[r1][c1] = 'X'

def solve():
    if (r1, c1) == (r2, c2):
        return 'YES'
    
    while q:
        cr, cc = q.popleft()

        if (cr, cc) == (r2, c2):

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < n and 0 <= nc < m and mp[nr][nc] == '.':
                    return 'YES'
            return 'NO'

        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if 0 <= nr < n and 0 <= nc < m and mp[nr][nc] == '.':
                mp[nr][nc] = 'X'
                q.append((nr, nc))
            elif 0 <= nr < n and 0 <= nc < m and mp[nr][nc] == 'X' and (nr, nc) == (r2, c2):
                return 'YES'

    return 'NO'

answer = solve()
print(answer)