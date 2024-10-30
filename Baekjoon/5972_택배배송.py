from heapq import heappop, heappush

N, M = map(int, input().split())  # 도착, 길
route = [[] for _ in range(50001)]
min_feed = [float('inf')] * 50001

for _ in range(M):
    s, e, f = map(int, input().split())
    route[s].append((f, e))
    route[e].append((f, s))

pq = [(0, 1)]  # 먹이, 노드

while pq:

    feed, cur = heappop(pq)

    if cur == N:
        print(feed)
        exit(0)

    if min_feed[cur] < feed:
        continue

    # 현재 위치에서 갈 수 있는 노드와 비용 뽑아오기
    for next_feed, next in route[cur]:
        new_feed = next_feed + feed

        if new_feed < min_feed[next]:
            heappush(pq, (new_feed, next))
            min_feed[next] = new_feed