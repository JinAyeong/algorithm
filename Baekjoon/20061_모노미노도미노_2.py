N = int(input())

red = [[0] * 4 for _ in range(4)]
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

for _ in range(N):
    t, x, y = map(int, input().split())