from collections import deque

N, M, K, X = map(int, input().split())  # 도시수, 도로수, 거리, 출발도시번호

adjl = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)

Q = deque([(0, X)])
distance[X] = 0

while Q:
    now_dist, now_city = Q.popleft()

    # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
    # now 가 이미 더 짧은 거리로 온 적이 있다면 pass
    for next_city in adjl[now_city]:
        new_dist = now_dist + 1

        if new_dist >= distance[next_city]:
            continue

        distance[next_city] = new_dist
        Q.append((new_dist, next_city))

result = False

for city in range(1, N+1):
    if distance[city] == K:
        result = True
        print(city)

if not result:
    print(-1)