
while True:

    N = int(input())

    if N == 0:
        break

    visited = [False] * N
    friends = {}

    for _ in range(N):
        name1, name2 = map(str, input().split())
        friends[name1] = name2