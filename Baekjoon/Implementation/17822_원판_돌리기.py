N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]

'''
3 1 1 2
1 2 1 3
'''

def turn(x, d, k):  # x의 배수인 원판을 d(0: 시계, 1: 반시계) 방향으로 k칸 회전
    for i in range(x, N+1, x):
        if d == 0:  # 시계 방향
            circles[i-1] = circles[i-1][-k:] + circles[i-1][:-k]
        else:  # 반시계 방향
            circles[i-1] = circles[i-1][k:] + circles[i-1][:k]

def number_delete():
    deleted = False
    to_delete = set()

    for i in range(N):
        for j in range(M):
            if circles[i][j] == 0:
                continue

            num = circles[i][j]
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, (j + dj) % M

                if 0 <= ni < N and circles[ni][nj] == num:
                    to_delete.add((i, j))
                    to_delete.add((ni, nj))

    if to_delete:
        deleted = True
        for i, j in to_delete:
            circles[i][j] = 0

    return deleted

def number_control():
    total = sum(sum(circles[i]) for i in range(N))
    count = sum(1 for i in range(N) for j in range(M) if circles[i][j] > 0)

    if count == 0:
        return

    average = total / count  # 0을 제외한 평균값

    for i in range(N):
        for j in range(M):
            if circles[i][j] > 0:
                if circles[i][j] > average:
                    circles[i][j] -= 1
                elif circles[i][j] < average:
                    circles[i][j] += 1

for _ in range(T):

    # 1. 원판 회전
    x, d, k = map(int, input().split())
    turn(x, d, k)

    # 2-1. 인접하면서 같은 수가 있는 경우에 그 수 삭제
    if number_delete():
        continue

    # 2-2. 인접하면서 같은 수가 없는 경우에 원판 수의 합보다 작은 수는 += 1 큰 수는 -= 1
    number_control()

print(sum(sum(line) for line in circles))