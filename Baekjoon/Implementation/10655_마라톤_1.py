N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]

cur = pos[0]
total_dist = 0

# 총 거리 및 위치 구하기
for i in range(1, N):
    x, y = pos[i]
    total_dist += abs(cur[0] - x) + abs(cur[1] - y)
    cur = [x, y]

result = float('inf')

# 하나씩 없애보기
for j in range(1, N - 1):
    a = abs(pos[j - 1][0] - pos[j][0]) + abs(pos[j - 1][1] - pos[j][1])
    b = abs(pos[j + 1][0] - pos[j][0]) + abs(pos[j + 1][1] - pos[j][1])
    c = abs(pos[j + 1][0] - pos[j - 1][0]) + abs(pos[j + 1][1] - pos[j - 1][1])

    new_dist = total_dist - (a + b) + c
    result = min(result, new_dist)

print(result)
