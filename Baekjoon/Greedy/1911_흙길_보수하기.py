N, L = map(int, input().split()) # 웅덩이 수, 널빤지 길이

water = [tuple(map(int, input().split())) for _ in range(N)]  # 웅덩이 시작점, 끝점
water.sort()

cnt = 0
cur_end = -1

for start, end in water:

    # 널빤지 시작점 구하기
    cur_start = max(start, cur_end)

    length = end - cur_start

    # 안붙여도 되면 continue
    if length <= 0:
        continue

    # 널빤지 딱 맞는지 확인 후, 안맞으면 하나 더 추가
    last = length % L

    cur_cnt = length // L
    if last != 0:
        cur_cnt += 1

    # 끝점 널빤지 붙인 칸으로 갱신
    cur_end = cur_start + cur_cnt * L
    cnt += cur_cnt

print(cnt)