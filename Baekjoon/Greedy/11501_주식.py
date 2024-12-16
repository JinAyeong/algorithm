# 현재 > max(미래주가) 라면 result += {max(미래주가) - 현재)
# 아니면 continue
# max(price[i+1:]) -> 시간초과
# 뒤에서부터 최댓값 갱신하면서 거꾸로 순환

for tc in range(int(input())):

    N = int(input())
    price = list(map(int, input().split()))
    max_price = price[N-1]
    result = 0

    for i in range(N-1, -1, -1):

        if price[i] < max_price:
            result += (max_price - price[i])

        else:
            max_price = price[i]

    print(result)