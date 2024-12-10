from collections import deque

N, M = map(int, input().split())  # 사다리, 뱀 수
ladders = {}
snakes = {}

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

min_move = 100

Q = deque([(0, 1)])  # 주사위 굴린 수, 현재 위치
min_each = [100] * 101

while Q:
    move, cur = Q.popleft()
    if cur == 100:
        min_move = min(min_move, move)

    # 사다리 있는지 확인
    if cur in ladders:
        min_each[cur] = min(min_each[cur], move)
        Q.append((move, ladders[cur]))
        continue

    # 뱀 있는지 확인
    if cur in snakes:
        min_each[cur] = min(min_each[cur], move)
        Q.append((move, snakes[cur]))
        continue
        
    # 없으면 주사위 굴리기
    for dice in range(1, 7):
        if cur + dice <= 100:
            if min_each[cur+dice] > move + 1:
                min_each[cur+dice] = move + 1
                Q.append((move + 1, cur + dice))

print(min_move)