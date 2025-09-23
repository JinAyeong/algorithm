'''
최고의 피자 : 1원당 열량이 가장 높은 피자 -> 가격은 낮고, 열량은 높은 피자
A : 도우의 가격
B : 토핑의 가격
피자의 열량 : 도우의 열량 (C) + 토핑의 열량 (D)
'''

N = int(input())
A, B = map(int, input().split())
C = int(input())
toppings = sorted((int(input()) for _ in range(N)), reverse=True)

calory = C
cost = A
answer = calory / cost

for i in range(N):
    cur_cal = calory + toppings[i]
    cur_cost = cost + B

    if answer >= cur_cal / cur_cost:
        break

    calory = cur_cal
    cost = cur_cost
    answer = cur_cal / cur_cost

print(calory // cost)