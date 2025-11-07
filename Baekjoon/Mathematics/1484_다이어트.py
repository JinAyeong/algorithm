'''
G킬로그램 = 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것
cur > before
G = (cur + before) * (cur - before)
'''
from math import sqrt
from heapq import heappop, heappush

G = int(input())

def solve(x, y):
    if (x + y) % 2 == 0:
        a = (x + y) // 2
        b = x - a
        return max(a, b)
    return 0
    
answer = []

for i in range(1, int(sqrt(G)) + 1):
    if G % i != 0:
        continue

    a = i
    b = G // i

    # x는 더 큰 값(cur+before), y는 더 작은 값(cur-before)
    x, y = max(a, b), min(a, b)

    # (x+y)가 짝수여야 cur가 정수
    if (x + y) % 2 != 0:
        continue

    cur = (x + y) // 2
    before = (x - y) // 2

    if before > 0:
        heappush(answer, cur)

if answer:
    while answer:
        print(heappop(answer))
else:
    print(-1)