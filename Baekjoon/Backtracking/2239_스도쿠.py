sdoku = [list(map(int, input().rstrip())) for _ in range(9)]
zero = []
row = [[False] * 10 for _ in range(9)]
column = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = sdoku[i][j]

        if num == 0:
            zero.append((i, j))
        else:
            row[i][num] = True
            column[j][num] = True
            box[(i//3)*3 + j//3][num] = True

N = len(zero)

def dfs(n):

    if n == N:
        for line in sdoku:
            print(''.join(map(str, line)))
        exit(0)
    
    x, y = zero[n]

    for num in range(1, 10):
        if not row[x][num] and not column[y][num] and not box[(x//3)*3 + y//3][num]:
            row[x][num] = True
            column[y][num] = True
            box[(x//3)*3 + y//3][num] = True
            sdoku[x][y] = num
            dfs(n + 1)
            row[x][num] = False
            column[y][num] = False
            box[(x//3)*3 + y//3][num] = False
            sdoku[x][y] = False

dfs(0)

#########################################################################################
# 시간초과

# import sys
# from collections import Counter

# input = sys.stdin.readline

# def check(arr, i, j):
#     # 행 체크
#     row = Counter(arr[i])
#     row[0] = 0
#     if not all(v <= 1 for v in row.values()):
#         return False

#     # 열 체크
#     column = Counter([arr[r][j] for r in range(9)])
#     column[0] = 0
#     if not all(v <= 1 for v in column.values()):
#         return False
    
#     # 박스 체크
#     sr, sc = (i // 3) * 3, (j // 3) * 3
#     box = Counter(arr[r][c] for r in range(sr, sr+3) for c in range(sc, sc+3))
#     box[0] = 0
#     if not all(v <= 1 for v in box.values()):
#         return False

#     return True

# def dfs(arr, i, j):

#     if j == 9:
#         i += 1
#         j = 0
#     if i == 9:
#         for row in arr:
#             print(''.join(map(str, row)))
#         exit(0)

#     if arr[i][j] != 0:
#         dfs(arr, i, j+1)
#     else:
#         for num in range(1, 10):
#             arr[i][j] = num
#             if check(arr, i, j):
#                 dfs(arr, i, j+1)
#             arr[i][j] = 0

# sdoku = [list(map(int, input().rstrip())) for _ in range(9)]
# dfs(sdoku, 0, 0)