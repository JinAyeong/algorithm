'''
타겟 // 2 == 1이 될 떄 까지 계속 반복
'''

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
visited = [False] * (N + 1)

for _ in range(Q):
    target = int(input())
    cur = target
    block = 0

    while cur != 0:
        if visited[cur]:
            block = cur
        cur //= 2

    print(block)

    if block == 0:
        visited[target] = True

