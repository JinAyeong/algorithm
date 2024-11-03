# 브루트포스, 백트래킹

N = int(input())  # 식재료 수
nutrient = list(map(int, input().split()))   # 최소 영양소
each_nutrient = [list(map(int, input().split())) for _ in range(N)]  # 각 식재료의 영양소와 가격
min_money = float('inf')
min_food_num = []


def choose(n, money, food_num, cur_nutrient):   # 현재 비용, 선택된 식재료 index
    global min_money, min_food_num, nutrient

    # n에 도달했으면 조건 확인하고 return
    if n == N:

        correct = True

        for i in range(4):
            if cur_nutrient[i] < nutrient[i]:
                correct = False
                return

        if min_money > money and correct:
            min_money = money
            min_food_num = food_num

        return

    # 최소가 아니면 return
    if min_money <= money:
        return

    # n을 선택하는 경우
    if set(each_nutrient[n]) != {0}:
        new_nutrient = [sum(values) for values in zip(cur_nutrient, each_nutrient[n][:4])]
        choose(n+1, money + each_nutrient[n][4], food_num + [n+1], new_nutrient)

    # n을 선택하지 않는 경우
    choose(n + 1, money, food_num, cur_nutrient)

choose(0, 0, [], [0, 0, 0, 0])


if min_money == float('inf'):
    print(-1)
else:
    print(min_money)
    print(*min_food_num)