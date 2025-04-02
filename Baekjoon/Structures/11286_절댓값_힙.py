import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            a_num, num = heappop(heap)
            print(num)
        else:
            print(0)

    else:
        heappush(heap, (abs(x), x))