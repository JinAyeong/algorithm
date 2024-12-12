from heapq import heappop, heappush

N, M, X = map(int, input().split())  # N명의 학생, M개의 단방향 도로, 파티장소

adjl = [[] for _ in range(N+1)]

for i in range(M):

    s, e, t = map(int, input().split())  # 시작마을, 도착마을, 소요시간

    adjl[s].append((e, t))


result = 0

def time_calculator(start, end):

    visited = [float('inf')] * (N+1)
    visited[start] = 0

    pq = [(0, start)]  # 시간, 마을 번호

    while pq:

        cur_time, cur = heappop(pq)

        if cur == end:
            return cur_time
        
        if visited[cur] < cur_time:
            continue

        for next, time in adjl[cur]:

            if visited[next] > cur_time + time:
                visited[next] = cur_time + time
                heappush(pq, (cur_time + time, next))



for i in range(1, N+1):

    if i == X:
        continue

    i_time = time_calculator(i, X) + time_calculator(X, i)
    result = max(i_time, result)


print(result)