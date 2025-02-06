N = int(input())

score = [list(input().split()) for _ in range(N)]

score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in score:
    print(name[0])