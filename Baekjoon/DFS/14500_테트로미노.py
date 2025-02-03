N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j, cur_sum, lst):
    global result

    if len(lst) == 4:
        result = max(cur_sum, result)
        return

    if len(lst) == 1:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for c in range(4):
            temp_sum = 0
            temp_lst = []
            can =True
            for d in range(4):
                if c == d:
                    continue
                ni, nj = i + dir[d][0], j + dir[d][1]
                if 0 <= ni < N and 0 <= nj < M:
                    temp_lst.append((ni, nj))
                    temp_sum += paper[ni][nj]

                else:
                    can = False
                    break
            if can:
                dfs(ni, nj, temp_sum + cur_sum, lst + temp_lst)

    # 한줄로 탐색
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in lst:
            dfs(ni, nj, cur_sum + paper[ni][nj], lst+[(ni, nj)])


result = 0

for a in range(N):
    for b in range(M):
        dfs(a, b, paper[a][b], [(a, b)])

print(result)