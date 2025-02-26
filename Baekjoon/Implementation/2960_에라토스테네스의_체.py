N, K = map(int, input().split())
numbers = [True] * (N + 1)
numbers[0] = numbers[1] = False
cnt = 0

for cur in range(2, N + 1):
    if numbers[cur]:
        for i in range(cur, N + 1, cur):
            if numbers[i]:
                numbers[i] = False
                cnt += 1
                if cnt == K:
                    print(i)
                    exit(0)
