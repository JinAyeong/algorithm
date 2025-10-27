N, M = map(int, input().split())

mp = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y, l, f = map(int, input().split())
    
    for i in range(x+1, x+l+1):
        for j in range(y+1, y+l+1):
            mp[i][j] = f

for lin in mp:
    print(*lin)

prefix = [[0] * (N+1) for _ in range(N+1)]
prefix[1][1] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if (i, j) == (1, 1):
            continue
        
        is_new = 1 if (mp[i][j] != mp[i-1][j] and mp[i][j] != mp[i][j-1] and mp[i][j] != 0) else 0

        prefix[i][j] = is_new + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for lin in prefix:
    print(*lin)