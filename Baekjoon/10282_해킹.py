from heapq import heappush, heappop

for tc in range(int(input())):

    n, d, c = map(int, input().split())   # 컴퓨터 수, 의존성 수, 해킹당한 컴퓨터 번호

    hack = [float('inf')] * (n+1)
    hack[c] = 0
    computer = [[] for _ in range(n+1)]

    pq = [(0, c)]  # 시간, 컴퓨터 번호

    for _ in range(d):
        a, b, s = map(int, input().split())  # b 감염 후 s초후부터 a도 감염
        computer[b].append((a, s))

    while pq:

        cur_t, cur_c = heappop(pq)

        # 이미 더 짧은 경로가 존재하면 무시
        if cur_t > hack[cur_c]:
            continue

        for next_c, time in computer[cur_c]:
            if hack[next_c] > cur_t + time:
                hack[next_c] = cur_t + time
                heappush(pq, (cur_t + time, next_c))

    hacked_computer = (n+1) - hack.count(float('inf'))
    max_time = 0

    for h in hack:
        if h != float('inf'):
            max_time = max(max_time, h)

    print(hacked_computer, max_time)