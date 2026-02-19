N, M, H = map(int, input().split()) # 세로선 수, 가로선 수, 가로선을 놓을 수 있는 위치의 개수
ladder = [[False] * H for _ in range(N)] # ladder[i][j] : i번 세로선을 j번 가로선에서 연결하는지 여부

for _ in range(N):
    a, b = map(int, input().split()) # a번 가로선을 b번 세로선에서 연결
    ladder[b][a] = True
    ladder[b+1][a] = True

def can_move(i, j):
    return ladder[i][j]

def can_ladder(i, j):
    return ladder[i][j] and ladder[i-1][j]

