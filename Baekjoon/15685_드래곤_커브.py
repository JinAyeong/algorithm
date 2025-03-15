'''
0세대 드래곤 커브 : 길이가 1인 선분
1세대 드래곤 커브 : 0세대 드래곤 커브의 끝점 -> 90도 회전 -> 0세대 드래곤 커브
2세대 드래곤 커브 : 1세대 드래곤 커브의 끝점 -> 90도 회전 -> 1세대 드래곤 커브
3세대 드래곤 커브 : 2세대 드래곤 커브의 끝점 -> 90도 회전 -> 2세대 드래곤 커브
'''

N = int(input())

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 오른쪽, 위쪽, 왼쪽, 아래쪽
curves = [
    [0],
    [0, 1],
    [0, 1, 2, 1],
    [0, 1, 2, 1, 2, 3, 2, 1],
]
mp = [[False] * 100 for _ in range(100)]
result = 0

# 드래곤 커브
def dragon(x, y, d, g):
    


# 정사각형 체크
def check(i, j):

    if mp[i][j] and mp[i+1][j] and mp[i][j+1] and mp[i+1][j+1]:
        return True

    return False

for _ in range(N):
    x, y, d, g = map(int, input().split()) # 시작점, 방향, 커브 종류




for a in range(99):
    for b in range(99):
        if check(a, b):
            result += 1