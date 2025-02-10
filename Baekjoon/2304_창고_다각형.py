N = int(input())
storages = [list(map(int, input().split())) for _ in range(N)]

last_H = 0
last_L = storages[0][0]
result = 0

storages.sort()
top = max(storages, key=lambda x: x[1])
top_idx = [i for i, (_, h) in enumerate(storages) if h == top]

for i in range(top_idx[0]):
    L, H = storages[i]

    left = H
    right = H

    for l in range(i-1, -1, -1):
        if storages[l][1] >= left:
            left = storages[l][1]
        else:
            break

    if i < N-1:
        for r in range(i+1, N):
            if storages[r][1] >= right:
                right = storages[r][1]
            else:
                break

    result += last_H * (L - last_L)
    last_H = min(left, right)
    last_L = L

for i in range(N-1, top_idx[-1], -1):
    L, H = storages[i]

    left = H
    right = H

    for l in range(i-1, -1, -1):
        if storages[l][1] >= left:
            left = storages[l][1]
        else:
            break

    if i < N-1:
        for r in range(i+1, N):
            if storages[r][1] >= right:
                right = storages[r][1]
            else:
                break

    result += last_H * (L - last_L)
    last_H = min(left, right)
    last_L = L

print(result)