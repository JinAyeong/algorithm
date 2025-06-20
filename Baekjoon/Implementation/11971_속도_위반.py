N, M = map(int, input().split())
roads = [0] * 100
rides = [0] * 100

last = 0

for _ in range(N):
    length, speed = map(int, input().split())

    for i in range(last, last + length):
        roads[i] = speed

    last += length

last = 0

for _ in range(M):
    length, speed = map(int, input().split())

    for j in range(last, last + length):
        rides[j] = speed

    last += length

minus = [rides[k] - roads[k] if rides[k] - roads[k] > 0 else 0 for k in range(100)]
print(max(minus))