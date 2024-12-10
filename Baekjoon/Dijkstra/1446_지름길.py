from heapq import heappush, heappop

N, D = map(int, input().split()) # 지름길 수, 고속도로 길이

route = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)
distance[0] = 0

for _ in range(N):
    s, e, v = map(int, input().split())  # 지름길 시작, 끝, 거리
    if 0 <= e <= D:
        route[s].append((v, e))

# 지름길 말고 그냥 이동했을때!!!!
for i in range(D):
    route[i].append((1, i+1))

pq = []
heappush(pq, (0, 0))

while pq:
    cur_dist, cur_node = heappop(pq)

    # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
    # now 가 이미 더 짧은 거리로 온 적이 있다면 pass
    if distance[cur_node] < cur_dist:
        continue

    for next_dist, next_node in route[cur_node]:
        new_dist = next_dist + cur_dist

        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(distance[D])