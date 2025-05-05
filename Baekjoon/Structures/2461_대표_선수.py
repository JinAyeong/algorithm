'''
N개의 학급마다 M명의 학생
각 반에서 한 명씩 선발하여 그 학생의 능력치중 최솟값과 최댓값 차이가 최소가 되는 경우의 값 출력
'''

#------------------------------------------------
# 우선순위 큐 python 1544 ms, 70692 KB

import heapq

N, M = map(int, input().split())
arr = [sorted(map(int, input().split())) for _ in range(N)]

# 각 반의 첫 번째 학생을 우선순위 큐에 넣음
heap = []
max_val = 0  # 현재 선택된 학생들 중 최대 능력치
for i in range(N):
    heapq.heappush(heap, (arr[i][0], i, 0))  # (능력치, 반 번호, 그 반에서의 인덱스)
    max_val = max(max_val, arr[i][0])

answer = float('inf')

while True:
    min_val, row, idx = heapq.heappop(heap)
    answer = min(answer, max_val - min_val)

    # 다음 학생이 없다면 종료
    if idx + 1 == M:
        break

    next_val = arr[row][idx + 1]
    heapq.heappush(heap, (next_val, row, idx + 1))
    max_val = max(max_val, next_val)

print(answer)

#------------------------------------------------
# 투포인터 python 2612 ms, 133768 KB

from collections import defaultdict

N, M = map(int, input().split())
arr = []

for i in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        arr.append((num, i))

arr.sort()

left = 0
answer = float('inf')
cnt = defaultdict(int)
unique_classes = 0

for right in range(len(arr)):
    val, cls = arr[right]
    cnt[cls] += 1
    if cnt[cls] == 1:
        unique_classes += 1

    # 모든 반이 포함된 상태면 왼쪽 줄이기 시도
    while unique_classes == N:
        min_val, _ = arr[left]
        max_val, _ = arr[right]
        answer = min(answer, max_val - min_val)

        # 왼쪽 포인터 이동 준비
        cnt[arr[left][1]] -= 1
        if cnt[arr[left][1]] == 0:
            unique_classes -= 1
        left += 1

print(answer)
