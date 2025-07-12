from collections import Counter
from math import comb

S = input()
S_cnt = Counter(S)
handle_cnt = {}

for s in S:
    handle_cnt[s] = 0

N = int(input())

for _ in range(N):
    h = input()[0]
    if h in handle_cnt:
        handle_cnt[h] += 1

answer = 1

for key, value in list(handle_cnt.items()):
    answer *= comb(value, S_cnt[key])

print(answer)