# 빗물 차는 조건 : 양옆에서 가장 높은 값중 더 작은 값

H, W = map(int, input().split())  # 세로, 가로
blocks = list(map(int, input().split()))
height = [0] * W
result = 0

for i in range(1, W-1):

    # 오른쪽방향, 왼쪽방향으로 이동하면서 최댓값 탐색
    # 탐색하면서 끝에 도달했으면 멈추고 더 작은 값 찾기
    # 탐색하면서 높이가 H 나오면 반대쪽만 탐색

    left, right = 0, 0

    for l in range(i-1, -1, -1):
        if blocks[l] > left:
            left = blocks[l]

    for r in range(i+1, W):
        if blocks[r] > right:
            right = blocks[r]

    cur_height = min(left, right)

    if cur_height > blocks[i]:
        result += cur_height - blocks[i]

print(result)