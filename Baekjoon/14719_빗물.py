H, W = map(int, input().split())  # 세로, 가로
blocks = list(map(int, input().split()))
height = [0] * W

for i in range(1, W-1):

    cur_height = 0

    