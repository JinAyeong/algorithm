# BFS

# 코니
# 처음 위치 C에서 1초 후 1만큼 움직임
# 이후 가속이 붙어 매 초마다 이전 이동거리 + 1만큼 움직임
# 브라운
# B-1, B+1, B * 2 중 하나로 움직임
# 브라운 범위 내에서만 움직임 가능, 코니 범위 벗어나면 게임 끝
# 코니를 잡거나, 코니가 범위를 벗어나는데 걸리는 최소 시간

from collections import deque

c = 11
b = 2

def catch_me(cony_loc, brown_loc):
    answer = float('inf')

    q = deque([(0, brown_loc)])
    visited = [False] * 200001
    visited[brown_loc] = True

    while q:
        t, b = q.popleft()

        cur_c = cony_loc + t * (t + 1) // 2

        if cur_c == b:
            answer = min(answer, t)
            break
        
        for next in [b + 1, b - 1, b * 2]:
            if 0 <= next < 200001 and not visited[next]:
                visited[next] = True
                q.append((t + 1, next))

    if answer == float('inf'):
        out = 1
        while True:
            if 200000 < cony_loc + out * (out + 1) // 2:
                answer = out
                break
            out += 1

    return answer

print(catch_me(c, b))  # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))