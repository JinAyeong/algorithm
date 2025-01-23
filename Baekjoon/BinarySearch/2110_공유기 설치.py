N, C = map(int, input().split()) # 집, 공유기 수
# 가장 인접한 두 공유기 사이의 거리 가장 크기
# C개의 공유기를 채울동안 반복
# left house[0], right house[N-1]로 거리 설정 후 이분탐색하며 거리가 최대인 집 찾아서 설치

house = [int(input()) for _ in range(N)]
house.sort()

left = 1
right = house[N-1]
result = 0

while left <= right:

    mid = (left + right) // 2
    last = house[0] # 마지막 공유기 설치한 집의 위치
    count = 1

    # 집 수색하면서 거리가 mid 이상일 때만 그 집에 설치 (처음 집엔 무조건 설치하므로 1부터 수색)
    for i in range(1, N):
        if house[i] - last >= mid: # 거리가 최솟값보다 크면 설치
            last = house[i]
            count += 1

    # 공유기 충분하면 결과 갱신, 거리 늘림
    if count >= C:
        left = mid + 1
        result = mid

    # 공유기 모자라면 거리 좁힘
    else:
        right = mid - 1

print(result)