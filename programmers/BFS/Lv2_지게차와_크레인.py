# 1번 : 접근 가능한 컨테이너만 꺼내기
# 2번 : 모든 컨테이너 꺼내기
from collections import deque

def solution(storage, requests):
    global answer

    n = len(storage)
    m = len(storage[0])
    answer = n * m

    mp = [[""] * (m + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(m):
            mp[i + 1][j + 1] = storage[i][j]

    # 크레인
    def crane(char):
        global answer

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if mp[i][j] == char:
                    answer -= 1
                    mp[i][j] = ''

    # 지게차
    def lift(char):
        global answer

        q = deque([(0, 0)])
        visited = [[False] * (m + 2) for _ in range(n + 2)]

        while q:

            i, j = q.popleft()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    if mp[ni][nj] == '':
                        q.append((ni, nj))
                    elif mp[ni][nj] == char:
                        answer -= 1
                        mp[ni][nj] = ''

    for request in requests:
        if len(request) == 2:
            crane(request[0])
        else:
            lift(request)

    return answer