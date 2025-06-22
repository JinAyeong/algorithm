def solve(points):

    # 변의 길이 판별
    for i in range(4):
        point1 = points[i-1]
        point2 = points[i]

        length = abs(point1[0] - point2[0])

T = int(input())

for _ in range(T):
    points = [list(map(int, input().split())) for _ in range(4)]

    print(solve(points))