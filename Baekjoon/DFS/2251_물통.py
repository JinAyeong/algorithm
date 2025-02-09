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
    cur_a, cur_b = pour(A, a, B, b)
    water(cur_a, cur_b, c)

    # a -> c
    cur_a, cur_c = pour(A, a, C, c)
    water(cur_a, b, cur_c)

    # b -> c
    cur_b, cur_c = pour(B, b, C, c)
    water(a, cur_b, cur_c)

    # b -> a
    cur_b, cur_a = pour(B, b, A, a)
    water(cur_a, cur_b, c)

    # c -> a
    cur_c, cur_a = pour(C, c, A, a)
    water(cur_a, b, cur_c)

    # c -> b
    cur_c, cur_b = pour(C, c, B, b)
    water(a, cur_b, cur_c)


def pour(x, x_water, y, y_water):

    if y == y_water:
        return x_water, y_water

    elif y - y_water > x_water:
        return 0, x_water + y_water

    elif y - y_water < x_water:
        return x_water - (y - y_water), y

    elif y - y_water == x_water:
        return 0, y

water(0, 0, C)

result.sort()
print(*result)