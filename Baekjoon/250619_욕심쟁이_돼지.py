'''
매일 사료 N만큼 배달
다음날 필요한 사료의 양 = 오늘 먹은 사료의 양 * 4
'''

T = int(input())

def solve(N, meals):
    day = 1
    total = sum(meals)

    while total <= N:
        total *= 4
        day += 1

    return day

for _ in range(T):
    N = int(input())
    meals = list(map(int, input().split()))
    print(solve(N, meals))