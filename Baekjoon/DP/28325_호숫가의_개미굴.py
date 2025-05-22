'''
- 쪽방이 있다면 쪽방 먼저 전부 채우기
- 쪽방을 먼저 다 채운 후에 방 채우기
    1. 만약에 현재 인덱스에 쪽방이 있다면, 현재 인덱스에 개미 x
    2. 만약 현재 인덱스에 쪽방이 없다면, 이전 인덱스에서 최댓값 가져오기
'''

N = int(input())
rooms = list(map(int, input().split()))

# dp1: 첫 방에 개미를 둔 경우 (마지막 방은 개미 못 둠)
dp1 = [[-float('inf'), -float('inf')] for _ in range(N)]
# dp2: 첫 방에 개미를 안 둔 경우 (마지막 방에 개미 둬도 됨)
dp2 = [[-float('inf'), -float('inf')] for _ in range(N)]

# 첫 방 개미 있음
if rooms[0] == 0:
    dp1[0] = [0, 1]
else:
    dp1[0] = [0, -float('inf')]

dp2[0] = [0, 0]  # 첫 방에 개미 없음

# dp1 계산 (첫 방에 개미 있음)
for i in range(1, N):
    if rooms[i]:
        dp1[i][0] = max(dp1[i-1])
        dp1[i][1] = -float('inf')
    else:
        dp1[i][0] = max(dp1[i-1])
        dp1[i][1] = dp1[i-1][0] + 1

dp1[-1][1] = -float('inf')  # 마지막 방에 개미 못 둠 (첫 방에 개미 있음)

# dp2 계산 (첫 방에 개미 없음)
for i in range(1, N):
    if rooms[i]:
        dp2[i][0] = max(dp2[i-1])
        dp2[i][1] = -float('inf')
    else:
        dp2[i][0] = max(dp2[i-1])
        dp2[i][1] = dp2[i-1][0] + 1

print(sum(rooms) + max(max(dp1[-1]), max(dp2[-1])))