import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mp = [[0] * N for _ in range(N)]

for _ in range(M):
    X, Y, L, F = map(int, input().split())

    for x in range(X, X + L):
        for y in range(Y, Y + L):
            mp[x][y] = F

low = 0
high = N

def check(i, j, length):

    cur_fruit = set()
    for k in range(length):
        for l in range(length):
            cur_fruit.add(mp[i + k][j + l])
            if len(cur_fruit) > 2 or mp[i + k][j + l] == 0:
                return False

    return True

result = 0

while low <= high:

    mid = (low + high) // 2
    cur_result = False

    for i in range(0, N-mid+1):
        if cur_result:
            break
        for j in range(0, N-mid+1):
            if check(i, j, mid):
                cur_result = True

    if cur_result:
        result = mid
        low = mid + 1

    else:
        high = mid - 1

print(result ** 2)