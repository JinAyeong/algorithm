from collections import deque

# range(N, 0, -1) 을 뒤에서부터 거꾸로 순회하면서 카운트 저장

N = int(input())
dp = [0] * (N + 1) # 계산 카운트
graph = [0] * (N + 1) # 이전 숫자

for i in range(N, 0, -1):

    cur_cnt = dp[i]

    # 1. X가 3으로 나누어 떨어지면, 3으로 나눈다
    if i % 3 == 0:
        cur_res = i // 3

        # 최솟값인지 확인 후 dp갱신
        if dp[cur_res] == 0 or dp[cur_res] > cur_cnt + 1:
            dp[cur_res] = cur_cnt + 1
            graph[cur_res] = i


    # 2. X가 2으로 나누어 떨어지면, 2으로 나눈다
    if i % 2 == 0:
        cur_res = i // 2

        # 최솟값인지 확인 후 dp갱신
        if dp[cur_res] == 0 or dp[cur_res] > cur_cnt + 1:
            dp[cur_res] = cur_cnt + 1
            graph[cur_res] = i

    # 3. 1을 뺀다
    cur_res = i - 1

    # 최솟값인지 확인 후 dp갱신
    if dp[cur_res] == 0 or dp[cur_res] > cur_cnt + 1:
        dp[cur_res] = cur_cnt + 1
        graph[cur_res] = i

print(dp[1])

# 지나온 숫자 찾기
lst = deque([])
current = 1

while current != 0:

    lst.appendleft(current)
    current = graph[current]

print(*lst)