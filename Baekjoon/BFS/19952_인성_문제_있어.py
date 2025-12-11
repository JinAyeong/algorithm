'''
가로 W, 세로 H -> 상하좌우로 이동 (힘 1 감소)
현재 
'''
from collections import deque

T = int(input())

for _ in range(T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())

    mp = [[0]*(W+1) for _ in range(H+1)]
    for _ in range(O):
        x, y, h = map(int, input().split())
        mp[x][y] = h

    visited = [[False]*(W+1) for _ in range(H+1)]
    q = deque([(Xs, Ys, F)])
    visited[Xs][Ys] = True
    
    answer = "인성 문제있어??"

    while q:
        x, y, f = q.popleft()

        if (x, y) == (Xe, Ye):
            answer = "잘했어!!"
            break

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if not (1 <= nx <= H and 1 <= ny <= W):
                continue
            
            # 높이 차이가 힘보다 크면 이동 불가
            if mp[nx][ny] - mp[x][y] > f:
                continue
            
            # 힘이 0보다 작아지면 이동 불가
            if f - 1 < 0:
                continue
            
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny, f - 1))

    print(answer)
