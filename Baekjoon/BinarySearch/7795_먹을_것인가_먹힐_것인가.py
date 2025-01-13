# 가로등의 높이만큼 주위를 비출 수 있음
# 최소 예산으로 굴다리의 모든 길을 밝힐 수 있는 높이 구하기

N = int(input())  # 굴다리 길이
M = int(input())  # 가로등 개수
spots = list(map(int, input().split()))  # 가로등 위치

# 가로등의 최대 높이 : N, 최소 높이 : 1
high = N + 1
low = 1

# 굴다리 검사
def light(h):

    global spots, N, M

    cur_end = 0

    for spot in spots:
        start, end = spot - h, spot + h

        if start > cur_end:
            return False
        else:
            cur_end = end

    if cur_end >= N:
        return True
    else:
        return False

result = N

# 이분탐색
while low <= high:

    cur = (low + high) // 2

    # 조건에 맞았으면 일단 result 현재 값으로 저장하고 더 밑에 값 탐색
    if light(cur):
        result = cur
        high = cur - 1
    # 조건에 안맞았으면 더 위에 값 탐색
    else:
        low = cur + 1

print(result)