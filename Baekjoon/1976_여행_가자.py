# dfs

import sys
sys.setrecursionlimit(10**6)

N = int(input())  # 도시 수
M = int(input())  # 여행 계획에 속한 도시 수
# [i][j] : i번 도시와 j번 도시의 연결 정보 (1이면 연결, 0이면 연결 안됨)
route = [list(map(int, input().split())) for _ in range(N)]
city = list(map(int, input().split()))

visited = [True] * N
for v in city:
    visited[v-1] = False

def travel(i):

    if all(visited):
        return True

    # i와 연결된 도시 방문
    for j in range(N):
        if i == j:
            continue

        if route[i][j] == 1:
            route[i][j] = 2
            visited[j] = True
            if travel(j):
                return True
            route[i][j] = 1
            visited[j] = False

    return False

for c in city:
    visited[c-1] = True
    if travel(c-1):
        print('YES')
        exit(0)
    visited[c-1] = False

print('NO')