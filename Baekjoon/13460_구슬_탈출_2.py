'''
1. 보드 상하좌우로 욺직여서 구슬 이동
2, 빨간구슬만 빼내기
3. 빨간구슬 먼저 너비우선탐색 시작
4. 빨간구슬 한번 굴릴때마다(방향이 바뀔때마다) 그 방향으로 파란구슬도 너비우선탐색
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

def move(i, j, d):
    