# 로봇이 포인트 순서대로 이동: 같은 좌표 위에 있으면 충돌 += 1
# 충돌 횟수 return
# points[i] = i + 1 번 포인트의 (r, c)
# routes[i] = i + 1 번 로봇의 운송 경로, (routes[i]의 길이는 모두 같음)

def solution(points, routes):  # 포인트들, 로봇 이동 경로

    answer = 0
    n = len(points)  # 포인트 수
    m = len(routes)  # 로봇 수
    length = len(routes[0])  # 로봇 인덱스 = length 되면 이동 끝
    robots = [list(points[x[0] - 1]) for x in routes]  # 로봇의 현재 위치
    index = [0] * m
    finish = 0

    # 초기 위치
    p = {}
    for robot in robots:
        if str(robot) in p:
            p[str(robot)] += 1
        else:
            p[str(robot)] = 1

    for c in p.values():
        if c > 1:
            answer += 1

    while finish < m:

        positions = {}

        for r in range(m):

            if index[r] == length - 1:
                continue

            robot = robots[r]  # 현재 위치
            next_index = index[r] + 1  # 다음 목적지 인덱스
            next_position = points[routes[r][next_index] - 1]  # 다음 목적지

            # 로봇 이동
            if robot[0] != next_position[0]:
                if robot[0] < next_position[0]:
                    robot[0] += 1
                elif robot[0] > next_position[0]:
                    robot[0] -= 1

            elif robot[1] != next_position[1]:
                if robot[1] < next_position[1]:
                    robot[1] += 1
                elif robot[1] > next_position[1]:
                    robot[1] -= 1

            # 다음 포지션에 도착했다면 또 다음 포지션으로
            if robot == next_position:
                index[r] += 1

            # 다 이동했을때 finish += 1
            if index[r] == length - 1:
                finish += 1

            robots[r] = robot

            # 충돌 검사를 위한 카운팅
            if str(robot) in positions:
                positions[str(robot)] += 1
            else:
                positions[str(robot)] = 1

        # 충돌 검사
        for cnt in positions.values():

            if cnt > 1:
                answer += 1

    return answer