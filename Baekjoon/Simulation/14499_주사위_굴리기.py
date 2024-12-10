# (r, c) : (북쪽으로부터 떨어진 칸의 개수, 서쪽으로부터 떨어진 칸의 개수)
# 이동한 칸에 쓰인 수가 0 : 칸의 수 = 주사위 바닥 수
# 이동한 칸에 쓰인 수가 0이 아님 : 주사위 바닥 수 = 칸의 수, 칸의 수 = 0
# result = 주위 상단의 값
# 바깥으로 이동할경우 무시

N, M, x, y, K = map(int, input().split()) # 세로, 가로, x, y, 명령 수
map_arr = [list(map(int, input().split())) for _ in range(N)] # 지도
turn = list(map(int, input().split())) # 주사위 순서 (1:동, 2:서, 3:북, 4:남)
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동, 서, 북, 남
position = (x, y)
dice = [0, 0, 0, 0, 0, 0]  # 북, 서, 아래, 동, 남, 위 (2, 4, 6, 3, 5, 1)
#   2
# 4 6 3
#   5
#   1

def update_dice(a, b):
    global position, dice, map_arr

    # 이동한 칸에 쓰인 수가 0 : 칸의 수 = 주사위 바닥 수
    if map_arr[a][b] == 0:
        map_arr[a][b] = dice[2]
        
    # 이동한 칸에 쓰인 수가 0이 아님 : 주사위 바닥 수 = 칸의 수, 칸의 수 = 0
    else:
        dice[2] = map_arr[a][b]
        map_arr[a][b] = 0

    print(dice[5])
    position = (a, b)

    return


for t in turn:
    
    nx, ny = position[0] + d[t][0], position[1] + d[t][1]
    
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    if t == 1:   # 동쪽으로 이동
        dice = [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]

    elif t == 2:   # 서쪽으로 이동
        dice = [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
    
    elif t == 3:   # 북쪽으로 이동
        dice = [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]

    elif t == 4:   # 남쪽으로 이동
        dice = [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]

    update_dice(nx, ny)