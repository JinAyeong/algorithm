def calculator(first_time, second_time, type):

    result = [0, 0]

    if type == '+':
        result[0] = first_time[0] + second_time[0]
        result[1] = first_time[1] + second_time[1]

    elif type == '-':
        result[0] = first_time[0] - second_time[0]
        result[1] = first_time[1] - second_time[1]

    if result[1] < 0:
        result[0] -= 1
        result[1] += 60

    if result[1] > 59:
        result[0] += 1
        result[1] -= 60

    return result


N = int(input())
goals = [list(input().split()) for _ in range(N)]
goals.append([0, '48:00'])

score = {1: 0, 2: 0}
time_1, time_2 = [0, 0], [0, 0]
win = 0
last_time = [0, 0]

for team, time in goals:

    minute, second = map(int, time.split(':'))
    team = int(team)

    win_time = calculator([minute, second], last_time, '-')

    if win == 1:
        time_1 = calculator(time_1, win_time, '+')

    elif win == 2:
        time_2 = calculator(time_2, win_time, '+')


    # 점수, 시간 갱신
    if team != 0:
        score[team] += 1

    if score[1] > score[2]:
        win = 1
    elif score[2] > score[1]:
        win = 2
    else:
        win = 0

    last_time = [minute, second]

print(f'{str(time_1[0]).zfill(2)}:{str(time_1[1]).zfill(2)}')
print(f'{str(time_2[0]).zfill(2)}:{str(time_2[1]).zfill(2)}')