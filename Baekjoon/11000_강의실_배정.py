from heapq import heappush, heappop, heapify

N = int(input())  # 강의실 수
lectures = [list(map(int, input().split())) for _ in range(N)]

lectures.sort(key=lambda x: (x[0], x[1]))  # 강의실 정렬

heap = []  # 강의 끝나는 시간 (빠른순)

for start, end in lectures:

    # heap[0] <= 현재 강의 시작시간이라면
    if heap and heap[0] <= start:
        # 강의실 이어붙이기 (pop 하고 조건문 밖에서 새로 추가)
        heappop(heap)

    # 조건에 맞지 않으면 강의실 새로 추가
    heappush(heap, end)

print(len(heap))