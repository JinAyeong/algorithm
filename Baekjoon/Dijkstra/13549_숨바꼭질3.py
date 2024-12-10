from heapq import heappop, heappush

N, K = map(int, input().split())

distance = [int(1e9)] * 100002
move = [[] for _ in range(100002)]

for i in range(100002):
    # 한칸아래
    if i+1 <= 100001:
        move[i].append((1, i+1))
    # 항칸위
    if i-1 >= 0:
        move[i].append((1, i-1))
    # 두배
    if i*2 <= 100001:
        move[i].append((0, i*2))

pq = []
heappush(pq, (0, N))
distance[N] = 0

while pq:
    cur_dist, cur_node = heappop(pq)

    if cur_dist > distance[cur_node]:
        continue

    for next_dist, next_node in move[cur_node]:
        new_dist = next_dist + cur_dist

        if 0 <= next_node <= 100001 and new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(distance[K])