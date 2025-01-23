from heapq import heapify, heappop, heappush

N = int(input())
arr = list(map(int, input().split()))
heapify(arr)

for _ in range(N-1):

    numbers = list(map(int, input().split()))

    for i in range(N):
        heappush(arr, numbers[i])
        heappop(arr)

print(arr[0])