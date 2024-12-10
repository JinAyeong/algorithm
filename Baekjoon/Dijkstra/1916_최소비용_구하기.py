from heapq import heappush, heappop

N = int(input())  # 도시 수
M = int(input())  # 버스 수

bus_info = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())  # 출발, 도착, 비용
    bus_info[s].append((v, e))

start, end = map(int, input().split())

distance = [int(1e9)] * (N+1)
distance[start] = 0

pq = []
heappush(pq, (0, start))

while pq:
    dist, now = heappop(pq)

    if distance[now] < dist:
        continue

    for next_dist, next_node in bus_info[now]:

        new_dist = next_dist + dist

        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(distance[end])