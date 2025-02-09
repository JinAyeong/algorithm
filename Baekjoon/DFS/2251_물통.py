# DFS

A, B, C = map(int, input().split())

result = []
case = set()

def water(a, b, c):

    if (a, b, c) in case:
        return

    if a == 0:
        result.append(c)

    case.add((a, b, c))

    # a -> b
    cur_a, cur_b = pour(a, B, b)
    water(cur_a, cur_b, c)

    # a -> c
    cur_a, cur_c = pour(a, C, c)
    water(cur_a, b, cur_c)

    # b -> c
    cur_b, cur_c = pour(b, C, c)
    water(a, cur_b, cur_c)

    # b -> a
    cur_b, cur_a = pour(b, A, a)
    water(cur_a, cur_b, c)

    # c -> a
    cur_c, cur_a = pour(c, A, a)
    water(cur_a, b, cur_c)

    # c -> b
    cur_c, cur_b = pour(c, B, b)
    water(a, cur_b, cur_c)


# def pour(x, x_water, y, y_water):
#
#     if y == y_water:
#         return x_water, y_water
#
#     elif y - y_water > x_water:
#         return 0, x_water + y_water
#
#     elif y - y_water < x_water:
#         return x_water - (y - y_water), y
#
#     elif y - y_water == x_water:
#         return 0, y

def pour(x_water, y, y_water): # 함수 최적화

    # 이동할 수 있는 물의 양 : x_water 전체, 또는 y 물통에 더 채울 수 있는 공간 중 더 작은 값
    move = min(x_water, y - y_water)

    return x_water - move, y_water + move

water(0, 0, C)

result.sort()
print(*result)