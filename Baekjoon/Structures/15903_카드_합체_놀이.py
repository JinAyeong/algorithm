from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)

for _ in range(m):
    c1 = heappop(cards)
    c2 = heappop(cards)
    new = c1 + c2
    heappush(cards, new)
    heappush(cards, new)

print(sum(cards))