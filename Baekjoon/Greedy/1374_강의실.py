from heapq import heappush, heappop, heapify

# 최소 필요한 강의실 수 출력

N = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[2]))

heap = []

for num, start, end in lectures:

    if heap and heap[0] <= start:
        heappop(heap)

    heappush(heap, end)

print(len(heap))