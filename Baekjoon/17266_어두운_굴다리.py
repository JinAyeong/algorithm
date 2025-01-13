# 가로등의 높이만큼 주위를 비출 수 있음
# 최소 예산으로 굴다리의 모든 길을 밝힐 수 있는 높이 구하기

N = int(input())  # 굴다리 길이
M = int(input())  # 가로등 개수
spots = list(map(int, input().split()))  # 가로등 위치

# 가로등의 최대 높이 : N, 최소 높이 : 1

high = N + 1
low = 1

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

result = None

while True:

    cur = (low + high) // 2

    cur_light = light(cur)
    cur_light_low = light(cur-1)

    if cur_light == True and cur_light_low == False:
        result = cur
        break

    if cur_light == True and cur_light_low == True:
        high = cur

    if cur_light == False and cur_light_low == False:
        low = cur

print(result)