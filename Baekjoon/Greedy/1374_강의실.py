from heapq import heappush, heappop, heapify

# 최소 필요한 강의실 수 출력
# 정렬하여 가장 빠른 시작 시간의 강의 부터 체크
# heap에 강의실의 끝나는 시간 push
# 현재 강의 시작시간이 heap[0] (강의가 가장 빨리 끝나는 시간) 보다 늦으면 heappop하고 현재 강의 끝나는 시간 push
# 시작 시간이 제일 작은 순서부터 체크하므로 최적의 강의실 수 셀 수 있음

N = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[2]))
print(lectures)
heap = []

for num, start, end in lectures:

    if heap and heap[0] <= start:
        heappop(heap)

    heappush(heap, end)

print(len(heap))