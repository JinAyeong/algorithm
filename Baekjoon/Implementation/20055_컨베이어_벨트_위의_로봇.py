'''
1번칸 : 올리는 위치, N번칸 : 내리는 위치
로봇은 컨베이어 벨트 위에서 스스로 이동 가능
로봇 올리기 or 로봇 이동 : 해당 칸의 내구도 1 감소

1. 벨트 한칸씩 회전
2. 로봇은 벨트가 회전하는 방향으로 이동가능하면 스스로 이동
2-1. 이동가능한 경우 : 빈칸이고, 내구도 1 이상
3. 내구도가 0인 칸의 수 K개 이상 -> 종료
'''

from collections import deque

N, K = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))
robot = deque([False] * 2 * N)
answer = 0

while True:
    answer += 1

    # 1. 벨트 회전
    a = conveyor_belt.pop()
    conveyor_belt.appendleft(a)
    robot.pop()
    robot.appendleft(False)
    robot[N-1] = False

    # 2. 이동가능한 로봇 이동
    for mr in range(N-1, -1, -1):
        if conveyor_belt[mr] > 0 and robot[mr-1] and not robot[mr]:
            robot[mr-1] = False
            robot[mr] = True
            conveyor_belt[mr] -= 1

            if mr == N-1:
                robot[mr] = False

    # 3. 로봇 올리기
    if conveyor_belt[0] > 0:
        conveyor_belt[0] -= 1
        robot[0] = True

    # 이동가능 체크
    if conveyor_belt.count(0) >= K:
        break

print(answer)