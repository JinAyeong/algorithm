M = int(input()) # 조약돌 색상
stone = list(map(int, input().split())) # 조약돌 색깔별 수
K = int(input()) # 조약돌 랜덤 뽑기 수
A = 0
B = 1

for i in range(len(stone)):

    if stone[i] < K:
        continue

    cur = 1

    for j in range(stone[i], stone[i] - K, -1):
        cur *= j

    A += cur

for l in range(sum(stone), sum(stone) - K, -1):
    B *= l

print(A/B)