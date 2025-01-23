# 파이썬 340 ms, 32412 KB

turn = list(map(int, input().split()))

# graph[현재 칸 인덱스][] =  이동 가능한 다음 칸 인덱스
graph = [
    [1], [2], [3], [4], [5],
    [6, 21], [7], [8], [9], [10],
    [11, 24], [12], [13], [14], [15],
    [16, 26], [17], [18], [19], [20],
    [32], [22], [23], [29], [25],
    [29], [27], [28], [29], [30],
    [31], [20]
]

# 현재 칸 수에 대한 획득 점수
score = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 22,
    24, 28, 27, 26, 25,
    30, 35, 0
]

result = 0
figures = [0 for _ in range(4)]

def move(n, total_score):

    global result, figures

    if n == 10:
        result = max(total_score, result)
        return

    m = turn[n]  # 움직일 칸의 수

    for i in range(4):
        cur = figures[i]
        next = figures[i]

        if cur == 32: # 도착한 말이면 continue
            continue

        # 주사위 수만큼 이동
        for j in range(m):
            if j == 0:
                next = graph[next][-1]
            else:
                next = graph[next][0]

            if next == 32: # 이동 수 채우기 전에 도착했으면 break
                break

        # 중복 검사
        if next == 32 or (next not in figures):
            figures[i] = next
            move(n + 1, total_score + score[next])
            figures[i] = cur

move(0, 0)
print(result)

# ---------------------------------------------------------------
# 파이썬 1772 ms, 33576 KB
# from copy import deepcopy
#
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