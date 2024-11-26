import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]

# heap 구조로 변경
heapify(lectures)

classroom = [0] * N
cur_count = 0

# for i in range(N):
#



print(classroom)
print(cur_count)
