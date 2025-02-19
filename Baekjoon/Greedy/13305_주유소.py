N = int(input())
dist = list(map(int, input().split())) # 다음 도시까지의 거리
price = list(map(int, input().split())) # 리터당 가격 (1미터당 1리터의 기름 사용)

cur_price = price[0]
result = cur_price * dist[0]

# 현재 가격이 이전가격보다 낮으면 갱신
for i in range(1, N-1):
    if price[i] <= cur_price:
        cur_price = price[i]

    result += cur_price * dist[i]

print(result)