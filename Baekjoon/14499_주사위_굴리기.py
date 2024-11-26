# (r, c) : (북쪽으로부터 떨어진 칸의 개수, 서쪽으로부터 떨어진 칸의 개수)
# 이동한 칸에 쓰인 수가 0 : 주사위 바닥에 써있는 수 복사됨
# 이동한 칸에 쓰인 수가 0이 아님 : 써있는 수가 주사위 바닥에 복사, 칸의 수는 0
# result : 주사위 이동할때마다 상단에 써있는 값
# 바깥으로 이동할경우 무시

N, M, x, y, K = map(int, input().split()) # 세로, 가로, x, y, 명령 수
map_arr = [list(map(int, input().split())) for _ in range(N)] # 지도
turn = list(map(int, input().split())) # 주사위 순서 (1:동, 2:서, 3:북, 4:남)
cur_dice = (x, y)

# for t in turn: