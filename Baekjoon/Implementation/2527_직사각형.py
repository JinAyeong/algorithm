for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    x_overlap = min(p1, p2) - max(x1, x2)
    y_overlap = min(q1, q2) - max(y1, y2)

    if x_overlap < 0 or y_overlap < 0:
        print('d')
    elif x_overlap == 0 and y_overlap == 0:
        print('c')
    elif x_overlap == 0 or y_overlap == 0:
        print('b')
    else:
        print('a')