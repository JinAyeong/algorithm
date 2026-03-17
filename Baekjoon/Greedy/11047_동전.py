N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
answer = 0

for i in range(N-1, -1, -1):
    coin = coins[i]

    if coin <= K:
        answer += K // coin
        K %= coin

print(answer)