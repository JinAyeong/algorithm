N, K = map(int, input().split())
S = input()

dir = {
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0)
}

i, j = 0, 0

for k in range(N * 2):
    d = S[k % N]
    i += dir[d][0]
    j += dir[d][1]

    if i == 0 and j == 0:
        print('YES')
        break

else:
    print('NO')