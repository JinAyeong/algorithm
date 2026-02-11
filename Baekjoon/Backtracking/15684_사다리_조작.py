import sys
input = sys.stdin.readline

N, M, H = map(int, input().split()) # 세로선 수, 가로선 수, 가로선을 놓을 수 있는 위치의 개수
ladder = [[False] * (N+1) for _ in range(H+1)] # ladder[i][j] : i번 가로줄에서 j번 세로성과 j+1 세로선 연결

for _ in range(M):
    a, b = map(int, input().split()) # a번 가로선을 b번 세로선에서 연결
    ladder[a][b] = True

def check():
    for start in range(1, N + 1):
        k = start
        for i in range(1, H + 1):
            if ladder[i][k]:
                k += 1
            elif k > 1 and ladder[i][k - 1]:
                k -= 1
        if k != start:
            return False
    return True

answer = 4

def dfs(cnt, x):
    global answer

    if check():
        answer = min(answer, cnt)
        return
    if cnt == 3 or cnt >= answer:
        return

    for i in range(x, H + 1):
        for j in range(1, N):
            if not ladder[i][j] and not ladder[i][j - 1] and not ladder[i][j + 1]:
                ladder[i][j] = True
                dfs(cnt + 1, i)
                ladder[i][j] = False

dfs(0, 1)

print(answer if answer < 4 else -1)