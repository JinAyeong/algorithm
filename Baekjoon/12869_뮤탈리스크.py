from itertools import permutations

N = int(input())  # scv 수
heals = list(map(int, input().split()))

# 완전탐색
# 1. 최대 6가지 방법으로 순서대로 완전탐색하며 체력 줄이기
# 2. 모든 heals가 0이 되면 break

min_attack = float('inf')

def attack(broken, a, cur_heals):

    global heals, min_attack

    if broken == N:
        min_attack = min(min_attack, a)

    cases = permutations(range(N), N)

    for case in cases:

        new_arr = []

        for idx in case:
            if idx == 0:
                cur_heals[idx] - 9