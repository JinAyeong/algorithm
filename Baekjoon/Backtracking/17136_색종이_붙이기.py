# 종이를 순회하면서 1이 나오면 1~5개의 색종이 하나씩 붙여보기
# 종이 붙인 곳 2로 표시

paper = [list(map(int, input().split())) for _ in range(10)]

cnt = 0 # 가려야할 1의 수
paper_1 = []
paper_cnt = [0, 5, 5, 5, 5, 5]
visited = [[False] * 10 for _ in range(10)]

for a in range(10):
    for b in range(10):
        if paper[a][b] == 1:
            paper_1.append((a, b))
            cnt += 1

result = float('inf')

def dfs(m, n):
    global result

    if m == cnt:
        result = min(result, n)
        return n

    i, j = paper_1[m]

    # 이미 붙인 색종이면 다음 색종이로
    if visited[i][j]:
        dfs(m+1, n)
    # 붙여야하면 어떤 크기의 색종이 붙일지 정하기
    else:
        for c in range(5, 0, -1): # 색종이 크기 5~1까지
            if paper_cnt[c] <= 0:
                continue
            cover = []
            can = True

            # 색종이 붙일 수 있는지 확인
            for k in range(i, i + c):
                if not can: break

                for l in range(j, j + c):
                    if not (0 <= k < 10 and 0 <= l < 10) or paper[k][l] != 1:
                        can = False
                        break
                    cover.append((k, l))

            if can:
                # 색종이 붙이기
                for x, y in cover:
                    visited[x][y] = True
                    paper[x][y] = 2
                paper_cnt[c] -= 1 # 색종이 차감
                # 다음 색종이로
                dfs(m+1, n+1)
                # 색종이 띠어내기
                for x, y in cover:
                    visited[x][y] = False
                    paper[x][y] = 1
                paper_cnt[c] += 1 # 색종이 돌려놓기

dfs(0, 0)

if result == float('inf'):
    result = -1

print(result)