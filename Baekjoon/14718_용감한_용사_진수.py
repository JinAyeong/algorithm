'''
이기는 조건
1. 적의 힘 <= 진수의 힘
2. 적의 민첩 <= 진수의 민첩
3. 적의 지능 <= 진수의 지능
최소 k명의 병사를 이길 수 있게 하는 최소 스탯 포인트
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(N)]
used = []
answer = float('inf')

def calculate_min(used):

    return sum(max(stats[used[k]][s] for k in range(K)) for s in range(3))

def comb(i, n):

    global answer, used

    if n == K:
        answer = min(calculate_min(used), answer)
        return

    for j in range(i, N):
        if j not in used:
            used.append(j)
            comb(j, n+1)
            used.pop()

comb(0, 0)

print(answer)