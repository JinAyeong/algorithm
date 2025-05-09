'''
1. N개의 지역, M분의 횡단보도 주기 (1분마다 신호가 바뀜)
2. 이동하는 데 1분이 걸림
3. 0분에 시작해서 1번에서 N번까지 도착하는 최소 시간 출력
4. 계산 : 기본 다익스트라에서 현재 시점마다 초록불 켜지는 시간 구하여 가중치 계산하기
'''

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
adjl = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    adjl[s].append((e, i)) # 출발 노드, 도착 노드, 초록불 시작 시간
    adjl[e].append((s, i))

dist = [float('inf')] * (N+1)
dist[1] = 0

heap = [(0, 1)] # 걸린 시간, 현재 노드

while heap:

    cur_t, cur_n = heappop(heap)

    if cur_n == N:
        print(cur_t)
        break

    if dist[cur_n] < cur_t:
        continue

    for next_n, green_start in adjl[cur_n]:

        # 현재 시점에서 이 간선이 언제 초록불이 되는지 계산
        wait = (green_start - cur_t % M + M) % M
        next_t = cur_t + wait + 1

        if dist[next_n] > next_t:
            dist[next_n] = next_t
            heappush(heap, (next_t, next_n))