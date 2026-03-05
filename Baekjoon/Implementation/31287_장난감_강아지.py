N, K = map(int, input().split())
S = input()

horizon = vertical = 0

limit = min(K, N)

for _ in range(limit):
    for c in S:
        if c == 'U':
            vertical += 1
        elif c == 'D':
            vertical -= 1
        elif c == 'R':
            horizon += 1
        else:
            horizon -= 1

        if horizon == 0 and vertical == 0:
            print("YES")
            exit(0)

print("NO")