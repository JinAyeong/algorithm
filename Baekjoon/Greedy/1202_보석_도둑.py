'''
가방에 하나씩 보석 담기
현재 가방에 들어갈 수 있는 보석들 다 heap에 push
> 다 분류 했으면 그때 가장 비싼 보석 pop 하여 result에 추가
'''

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, K = map(int, input().split())  # 보석 수, 가방 수

jewelry = [list(map(int, input().split())) for _ in range(N)]   # 가격, 무게
bags = [int(input()) for _ in range(K)]     # 무게
result = 0

jewelry.sort()
bags.sort()
heap = []
idx = 0

for bag in bags:

    while idx < N and jewelry[idx][0] <= bag:
        heappush(heap, (-jewelry[idx][1], jewelry[idx][0]))
        idx += 1

    if heap:
        result += -heappop(heap)[0]

print(result)