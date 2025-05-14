'''
1. 좌표의 가장 위에 있는 블록 제거 -> 인벤토리에 넣기 : 2초
2. 인벤토리에서 블록 하나를 꺼냄 -> 좌표의 가장 위의 블록에 놓기 : 1초
- 땅을 전부 같은 높이로 고르는데 걸리는 시간과 해당 높이 출력
- 답이 여러개라면 가장 높은 높이 출력
'''

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

def minecraft(goal):
    put = pick = 0

    for i in range(N):
        for j in range(M):
            h = mp[i][j]
            if h < goal:
                put += (goal - h)
            else:
                pick += (h - goal)

    inventory = B + pick
    if inventory < put:
        return float('inf')
    return put * 1 + pick * 2

result = [float('inf'), 0]

for height in range(257):
    time = minecraft(height)
    if time <= result[0]:
        result = [time, height]

print(*result)
