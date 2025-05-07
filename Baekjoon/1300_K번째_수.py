N = int(input())
k = int(input())

arr = [[0] * N for _ in range(N)]

for i in range(1, 1+N):
    for j in range(1, 1+N):
        arr[i-1][j-1] = i * j

for line in arr:
    print(*line)