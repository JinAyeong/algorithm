'''
1. 보드 상하좌우로 욺직여서 구슬 이동
2. 너비무선탐색 한 방향으로만 진행
3. 파란구슬, 빨간구슬의 위치 저장
4. 보드 기울일때마다 파란구슬과 빨간구슬 그 방향으로 이동
5. 이동 순서는 방향에 따라서 정렬 후 우선순위대로 이동
6. 오른쪽: -j, 왼쪽: j, 위: i, 아래: -i 정렬
7. 10번 이하로 움직이기 (백트래킹)
'''

from collections import deque

N, M = map(int, input().split())
mp = [list(input()) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위, 아래, 왼쪽, 오른쪽
red = blue = goal = (0, 0)

# 구슬과 목적지 설정
for i in range(N):
    for j in range(M):
        if mp[i][j] == 'R':
            red = (i, j)
        elif mp[i][j] == 'B':
             blue = (i, j)
        elif mp[i][j] == 'O':
            goal = (i, j)

