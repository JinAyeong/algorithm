'''
상하좌우 중 하나로 두칸 이동 (뛰어넘기 가능)
'''

N, K = map(int, input().split())
dabbaba = set(tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K))

dir = [(-2, 0), (2, 0), (0, -2), (0, 2)]

answer = set()

for i, j in dabbaba:

    for di, dj in dir:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in dabbaba:
            answer.add((ni, nj))

print(len(answer))