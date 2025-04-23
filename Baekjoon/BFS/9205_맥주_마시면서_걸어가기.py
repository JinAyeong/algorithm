'''
50미터 가기 전에 한 병 마셔야 한다.
'''

from collections import deque

for _ in range(int(input())):
    n = int(input())  # 맥주를 파는 편의점 수
    mp = [tuple(map(int, input().split())) for _ in range(n+2)]
    visited = [False] * (n+2)

    def bfs():
        q = deque()
        q.append(0)
        visited[0] = True

        while q:
            cur = q.popleft()
            if cur == n + 1:
                return "happy"

            for i in range(n + 2):
                if not visited[i]:
                    dist = abs(mp[i][0] - mp[cur][0]) + abs(mp[i][1] - mp[cur][1])
                    if dist <= 50 * 20:
                        visited[i] = True
                        q.append(i)
        return "sad"

    print(bfs())

#------------------------------------------------------------------------------------
# 시간 초과 코드 dfs

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())  # 맥주를 파는 편의점 수
    mp = [tuple(map(int, input().split())) for _ in range(n+2)]
    visited = [False] * (n+2)
    visited[0] = True
    result = 'sad'

    def dfs(i):
        global result

        if i == n+1:
            result = 'happy'
            return

        for j in range(1, n+2):
            dist = abs(mp[j][0] - mp[i][0]) + abs(mp[j][1] - mp[i][1])
            if not visited[j] and dist <= 50 * 20:
                visited[j] = True
                dfs(j)
                visited[j] = False

    dfs(0)
    print(result)