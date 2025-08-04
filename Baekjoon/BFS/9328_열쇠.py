from collections import deque, defaultdict

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    mp = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    answer = 0

    keys = input()
    keys_dict = {}
    if keys != '0':
        for key in keys:
            keys_dict[key] = True

    q = deque()
    not_opened_door = defaultdict(list)

    # 가장자리 탐색
    def try_push(i, j):
        global answer
        if not (0 <= i < h and 0 <= j < w):
            return
        if visited[i][j] or mp[i][j] == '*':
            return
        cur = mp[i][j]
        visited[i][j] = True
        if cur == '$':
            answer += 1
            mp[i][j] = '.'
        elif cur.islower():
            keys_dict[cur] = True
            mp[i][j] = '.'
        elif cur.isupper():
            if cur.lower() in keys_dict:
                mp[i][j] = '.'
            else:
                not_opened_door[cur].append((i, j))
                return
        q.append((i, j))

    for i in range(h):
        try_push(i, 0)
        try_push(i, w - 1)
    for j in range(w):
        try_push(0, j)
        try_push(h - 1, j)

    # BFS
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            if visited[ni][nj] or mp[ni][nj] == '*':
                continue
            cur = mp[ni][nj]
            visited[ni][nj] = True

            if cur == '$':
                answer += 1
                mp[ni][nj] = '.'
                q.append((ni, nj))
            elif cur == '.':
                q.append((ni, nj))
            elif cur.islower():
                if cur not in keys_dict:
                    keys_dict[cur] = True
                    for dii, djj in not_opened_door[cur.upper()]:
                        q.append((dii, djj))
                        visited[dii][djj] = True
                    not_opened_door[cur.upper()] = []
                mp[ni][nj] = '.'
                q.append((ni, nj))
            elif cur.isupper():
                if cur.lower() in keys_dict:
                    mp[ni][nj] = '.'
                    q.append((ni, nj))
                else:
                    not_opened_door[cur].append((ni, nj))

    print(answer)
