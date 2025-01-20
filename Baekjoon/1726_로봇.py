from collections import deque

# 1: 갈수없음, 0: 갈수있음
# 명령1: 1, 2, 3 거리만큼 직진
# 명령2: 왼쪽 또는 오른쪽 90도 회전
# 저장할 값 : 현재방향, 명령 횟수

M, N = map(int, input().split()) # 세로, 가로
factory = [list(map(int, input().split())) for _ in range(M)]

start = list(map(int, input().split())) # 행, 열, 방향
end = list(map(int, input().split()))   # 1, 2, 3, 4 = 동, 서, 남, 북

d = [(-1, 0), (1, 0)]