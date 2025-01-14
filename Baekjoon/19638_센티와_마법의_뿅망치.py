# T 이하만큼 반복

from heapq import heappush, heappop

N, H, T = map(int, input().split())  # 인구수, 센티의 키, 뿅망치 횟수 제한
heap = []  # 최대힙
hammer = 0

for _ in range(N):
    height = int(input())
    heappush(heap, -height)

while heap:
    # 망치 다 썼으면 break
    if hammer == T:
        break

    # 다음 사람 : 가장 키가 큰 사람
    cur = -heap[0]

    # 가장 키가 큰 사람이 센티보다 작거나 1이면 break
    if cur < H or cur == 1:
        break

    # 뿅망치 효과가 있는 사람이면 뿅망치 떄리고 heappush, 망치 사용횟수 추가
    n = heappop(heap)
    heappush(heap, int(n / 2))
    hammer += 1


if -heap[0] < H:
    print('YES')
    print(hammer)
else:
    print('NO')
    print(-heap[0])