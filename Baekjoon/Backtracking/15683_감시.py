'''
0: 빈칸, 6: 벽, 1~5: CCTV
'''

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 오 아 왼
cctv = []

for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5:
            cctv.append((i, j, room[i][j]))

cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 감시
def watch(dirs, x, y, temp):
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += dir[d][0]
            ny += dir[d][1]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            if temp[nx][ny] == 6:
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = -1

result = float('inf')

def dfs(depth, temp):
    global result

    if depth == len(cctv):
        cnt = sum(row.count(0) for row in temp)
        result = min(result, cnt)
        return

    x, y, num = cctv[depth]
    for dirs in cctv_dir[num]:
        temp_copy = [row[:] for row in temp]
        watch(dirs, x, y, temp_copy)
        dfs(depth + 1, temp_copy)

dfs(0, room)
print(result)
