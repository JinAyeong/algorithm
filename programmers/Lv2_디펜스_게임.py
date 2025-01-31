

#----------------------------------
# backtracking 시간초과

import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, k, enemy):
    global answer
    answer = 0

    def defense(i, cur_n, cur_k, enemy):
        global answer

        if i == len(enemy) or (cur_n < enemy[i] and cur_k == 0):
            answer = max(answer, i)
            return

        # 무적권 사용
        if cur_k > 0:
            defense(i + 1, cur_n, cur_k - 1, enemy)

        # 무적권 사용 안함
        if cur_n - enemy[i] >= 0:
            defense(i + 1, cur_n - enemy[i], cur_k, enemy)

    defense(0, n, k, enemy)

    return answer