'''
서로가 서로를 잡을 수 없는 위치에 놓인 비숍의 최대 수
'''

# 성공 코드
# 흑백 따로 탐색

import sys
input = sys.stdin.readline

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]

visited_l = [False] * (2 * N - 1)
visited_r = [False] * (2 * N - 1)

black = []
white = []

for i in range(N):
    for j in range(N):
        if mp[i][j]:
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))

def dfs(arr, idx, cnt):
    if idx == len(arr):
        return cnt

    r, c = arr[idx]
    max_cnt = dfs(arr, idx + 1, cnt)

    if not visited_l[r - c] and not visited_r[r + c]:
        visited_l[r - c] = visited_r[r + c] = True
        max_cnt = max(max_cnt, dfs(arr, idx + 1, cnt + 1))
        visited_l[r - c] = visited_r[r + c] = False

    return max_cnt

result_black = dfs(black, 0, 0)
result_white = dfs(white, 0, 0)

print(result_black + result_white)

#--------------------------------------------------------
# 시간초과

import sys
input = sys.stdin.readline

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]

visited_l = [False] * (2 * N - 1)
visited_r = [False] * (2 * N - 1)

blank = []
blank_cnt = 0

for i in range(N):
    for j in range(N):
        if mp[i][j]:
            blank.append((i, j))
            blank_cnt += 1

def dfs(idx, cnt):

    if idx == blank_cnt:
        return cnt

    r, c = blank[idx]
    max_cnt = dfs(idx+1, cnt)

    if not visited_r[r+c] and not visited_l[r-c]:
        visited_r[r + c] = visited_l[r - c] = True
        max_cnt = max(max_cnt, dfs(idx+1, cnt+1))
        visited_r[r + c] = visited_l[r - c] = False

    return max_cnt

print(dfs(0, 0))