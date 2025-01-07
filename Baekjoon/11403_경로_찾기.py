from collections import deque

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

# (i, j) == 1 : i 에서 j로 가는 간선 존재
# (0, 0) : 0 -> 1, 1 -> 2, 2 -> 0 이므로 (0, 0) = 1

result = [[0] * N for _ in range(N)]

for i in range(N):

    Q = deque([i])

    while Q:
        cur = Q.popleft()

        for j in range(N):
            # print(G[cur][j], result[cur][j])

            if G[cur][j] == 1 and not result[i][j]:
                result[i][j] = 1
                Q.append(j)


for line in result:
    print(*line)