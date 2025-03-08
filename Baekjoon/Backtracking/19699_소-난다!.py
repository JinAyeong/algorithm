N, M = map(int, input().split()) # N마리의 소 M마리 선별
cows = list(map(int, input().split()))
cows.sort()
max_sum = sum(cows[N-M:])
is_prime = [True] * (max_sum + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, max_sum+1):
    if is_prime[i]:
        for j in range(i*2, max_sum + 1, i):
            is_prime[j] = False

result = []

# 소 선택
def select(i, j, cur_sum):

    if i == M:
        if is_prime[cur_sum] and cur_sum not in result:
            result.append(cur_sum)
        return

    if j == N-1:
        return

    for k in range(j+1, N):
        select(i + 1, k, cur_sum+cows[k])

for s in range(N):
    select(1, s, cows[s])

if result:
    result.sort()
    print(*result)
else:
    print(-1)
