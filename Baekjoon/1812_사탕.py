import sys
sys.setrecursionlimit(10**6)

N = int(input())

candy_sum = [int(input()) for _ in range(N)]
total = sum(candy_sum) // 2
candies = [0] * N

def dfs(i):

    if i == N:
        for c in range(N):
            if candies[(c+1) % N] + candies[c] != candy_sum[c]:
                return

        for candy in candies:
            print(candy)
        return

    for j in range(1, total):
        candies[i] = j
        dfs(i+1)
        candies[i] = 0

dfs(0)