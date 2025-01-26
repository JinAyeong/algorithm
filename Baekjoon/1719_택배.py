from heapq import heappop, heappush

n, m = map(int, input().split())

adjl = [[] for _ in range(n+1)]
result = [['-'] * n for _ in range(n)]

for _ in range(m):

    s, e, t = map(int, input().split())

    adjl[s].append((t, e))

heap = [(0, n, []) for _ in range(n)]

while heap:

    ct, cc, route = heappop(heap)

    for t, n in adjl[cc]:

        nt = ct + t
        n_route = route + [n]