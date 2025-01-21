from copy import deepcopy

result = 0

turn = list(map(int, input().split()))

dice = {
    10: [10, 13, 16, 19],
    20: [20, 22, 24],
    25: [25, 30, 35],
    30: [30, 28, 27, 26],
    40: [40]
}

figures = [(0, 0, 0, False) for _ in range(4)]  # 현재 위치, 0/10/20/30 정보, 10/20/30일 때 그 안의 인덱스, 도착 정보

def move(n, total_score):
    global result, figures, dice

    if n == 10:
        result = max(result, total_score)
        return

    i = turn[n]

    for f in range(4):
        figure = deepcopy(figures[f])
        cur = figures[f][0]
        inform = figures[f][1]
        index = figures[f][2]
        finish = figures[f][3]

        if finish:
            continue

        if inform == 0:
            plus = cur + i * 2 # 받을 점수

            if plus > 40:
                finish = True
                plus = 0

            elif plus % 5 == 0:
                inform = plus
                index = 0

        elif inform == 10 or inform == 20 or inform == 30:
            index = index + i

            if index >= len(dice[inform]):
                index -= len(dice[inform])
                inform = 25

                if index >= len(dice[inform]):
                    index -= len(dice[inform])
                    inform = 40

                    if index >= len(dice[inform]):
                        finish = True
                        plus = 0
                    else:
                        plus = dice[inform][index]

                else:
                    plus = dice[inform][index]
            else:
                plus = dice[inform][index]

        elif inform == 25 or inform == 40:
            index = index + i

            if index >= len(dice[inform]):
                index -= len(dice[inform])
                inform = 40

                if index >= len(dice[inform]):
                    finish = True
                    plus = 0

                else:
                    plus = dice[inform][index]

            else:
                plus = dice[inform][index]

        next_figure = (plus, inform, index, finish)

        can_use = True

        for c in range(4):
            if figures[c][3]:
                continue

            if figures[c][0] == plus and figures[c][1] == inform:
                can_use = False
                break

        if can_use:
            figures[f] = next_figure
            move(n+1, total_score + plus)
            figures[f] = figure

move(0, 0)

print(result)