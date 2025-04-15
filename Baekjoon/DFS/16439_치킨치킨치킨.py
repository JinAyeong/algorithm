N, M = map(int, input().split())
preference = [list(map(int, input().split())) for _ in range(N)]
result = 0

def comb(i, chickens):
    global result

    if len(chickens) == 3:
        total_preference = 0

        for n in range(N):
            cur_preference = max(map(lambda x: preference[n][x], chickens))
            total_preference += cur_preference

        result = max(total_preference, result)
        return

    for j in range(i+1, M):
        comb(j, chickens + [j])

comb(-1, [])

print(result)