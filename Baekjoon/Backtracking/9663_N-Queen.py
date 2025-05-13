import sys
input = sys.stdin.readline

N = int(input())

visited_l = [False] * (2 * N - 1)
visited_r = [False] * (2 * N - 1)
visited = [False] * N

def dfs(i):

    if i == N:
        return 1

    cnt = 0

    for j in range(N):

        if not visited_l[j + i] and not visited_r[j - i + N - 1] and not visited[j]:
            visited_l[j + i] = True
            visited_r[j - i + N - 1] = True
            visited[j] = True
            cnt += dfs(i+1)
            visited_l[j + i] = False
            visited_r[j - i + N - 1] = False
            visited[j] = False

    return cnt

print(dfs(0))