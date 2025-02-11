# 다익스트라

# 코니
# 처음 위치 C에서 1초 후 1만큼 움직임
# 이후 가속이 붙어 매 초마다 이전 이동거리 + 1만큼 움직임
# 브라운
# B-1, B+1, B * 2 중 하나로 움직임
# 브라운 범위 내에서만 움직임 가능, 코니 범위 벗어나면 게임 끝
# 코니를 잡거나, 코니가 범위를 벗어나는데 걸리는 최소 시간

from heapq import heappop, heappush

c = 11
b = 2

def catch_me(cony_loc, brown_loc):
    dp_1 = [float('inf')] * 200001
    dp_2 = [float('inf')] * 200001
    dp_1[cony_loc] = 0
    dp_2[brown_loc] = 0
    answer = float('inf')

    # 코니 이동
    for t in range(1, 1000000):
        move = t * (t+1) // 2

        if not (0 <= cony_loc + move < 200001):
            answer = t
            break

        dp_1[move + cony_loc] = t


    heap = [(0, brown_loc)]

    # 브라운 이동
    while heap:
        cur_t, cur_l = heappop(heap)

        cur_c = cony_loc + cur_t * (cur_t + 1) // 2

        if cur_t == cur_c:
            answer = min(cur_t, answer)

        if dp_2[cur_l] < cur_t:
            continue

        if 0 <= cur_l + 1 < 200001:
            if dp_2[cur_l + 1] > cur_t + 1:
                heappush(heap, (cur_t + 1, cur_l + 1))
                dp_2[cur_l + 1] = cur_t + 1

        if 0 <= cur_l - 1 < 200001:
            if dp_2[cur_l - 1] > cur_t + 1:
                heappush(heap, (cur_t + 1, cur_l - 1))
                dp_2[cur_l - 1] = cur_t + 1

        if 0 <= cur_l * 2 < 200001:
            if dp_2[cur_l * 2] > cur_t + 1:
                heappush(heap, (cur_t + 1, cur_l * 2))
                dp_2[cur_l * 2] = cur_t + 1

    return answer

print(catch_me(c, b))  # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))