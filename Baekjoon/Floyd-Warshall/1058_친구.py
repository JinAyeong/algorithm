'''
가장 유명한사람 : 2-친구가 가장 많은 사람
2-친구 되는법 : 서로 친구이거나, 겹지인 존재
'''

# 플로이드 워셜
# python 32412 KB 92 ms

N = int(input())
adjl = [input() for _ in range(N)]
dist = [[float('inf')] * N for _ in range(N)]

# 친구 관계 (Y면 거리 1, 본인은 거리 0)
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        elif adjl[i][j] == 'Y':
            dist[i][j] = 1

# 플로이드-워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 2-친구 수 계산
result = 0
for i in range(N):
    cnt = sum(1 for j in range(N) if i != j and dist[i][j] <= 2)
    result = max(result, cnt)

print(result)


#--------------------------------------------------
# 단순 그래프 탐색
# python 32412 KB 48 ms

N = int(input())
adjl = [input() for _ in range(N)]

def friend(a, b):
    if adjl[a][b] == 'Y':
        return True

    for f in range(N):
        if f == a or f == b:
            continue
        if adjl[f][a] == 'Y' and adjl[f][b] == 'Y':
            return True

    return False

result = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if friend(i, j):
            cnt += 1

    result = max(result, cnt)

print(result)