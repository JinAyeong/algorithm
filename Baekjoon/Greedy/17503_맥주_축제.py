# 우선순위 큐

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, K = map(int, input().split())  # 기간, 선호도의 합, 맥주 종류
beers = [list(map(int, input().split())) for _ in range(K)] # 선호도, 도수레벨
beers.sort(key=lambda x: x[1])

total = 0
heap = []
result = 0

for v, c in beers:
    if len(heap) < N:
        heappush(heap, (v, c))
        total += v

        if len(heap) == N:
            if total >= M:
                result = c
            else:
                total -= heappop(heap)[0]

print(result if result != 0 else -1)

#------------------------------------------------------------------------------
# 이분탐색

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())  # 기간, 선호도의 합, 맥주 종류
beers = [list(map(int, input().split())) for _ in range(K)] # 선호도, 도수레벨
beers.sort(reverse=True)

low = min(c for v, c in beers)
high = max(c for v, c in beers)
result = float('inf')

while low <= high:
    mid = (low + high) // 2
    total = 0
    cnt = 0

    for v, c in beers:
        if c <= mid:
            total += v
            cnt += 1
        if cnt == N:
            break

    if total >= M and cnt == N:
        result = mid
        high = mid - 1

    else:
        low = mid + 1

print(result if result != float('inf') else -1)