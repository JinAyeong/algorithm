'''
0세대 드래곤 커브 : 길이가 1인 선분
1세대 드래곤 커브 : 0세대 드래곤 커브의 끝점 -> 90도 회전 -> 0세대 드래곤 커브
2세대 드래곤 커브 : 1세대 드래곤 커브의 끝점 -> 90도 회전 -> 1세대 드래곤 커브
3세대 드래곤 커브 : 2세대 드래곤 커브의 끝점 -> 90도 회전 -> 2세대 드래곤 커브
'''

N = int(input())
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 오른쪽, 위쪽, 왼쪽, 아래쪽
mp = [[False] * 101 for _ in range(101)]
result = 0

# 드래곤 커브
def dragon(x, y, d, g):
    arr = [d]
    mp[x][y] = True

    for _ in range(g):
        for i in range(len(arr)-1, -1, -1):
            arr.append((arr[i] + 1) % 4)

    for nd in arr:
        x += direction[nd][0]
        y += direction[nd][1]

        if 0 <= x < 101 and 0 <= y < 101:
            mp[x][y] = True

# 정사각형 체크
def check(i, j):

    if mp[i][j] and mp[i+1][j] and mp[i][j+1] and mp[i+1][j+1]:
        return 1
    return 0

for _ in range(N):
    x, y, d, g = map(int, input().split()) # 시작점, 방향, 커브 종류
    dragon(x, y, d, g)

for a in range(100):
    for b in range(100):
        result += check(a, b)

print(result)