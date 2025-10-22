tc = 0

while True:
    tc += 1
    N = int(input())
    if N == 0:
        break

    manitto = {}
    visited = {}
    friends = []
    cycle = 0

    for _ in range(N):

        m1, m2 = input().split()
        manitto[m1] = m2
        visited[m1] = False
        friends.append(m1)

    def dfs(string):
        visited[string] = True
        if not visited[manitto[string]]:
            dfs(manitto[string])

    for friend in friends:
        if not visited[friend]:
            dfs(friend)
            cycle += 1

    print(f'{tc} {cycle}')