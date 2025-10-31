def solution(friends, gifts):
    n = len(friends)
    idx = {f: i for i, f in enumerate(friends)}

    # 주고받은 횟수
    grid = [[0] * n for _ in range(n)]
    for g in gifts:
        a, b = g.split()
        grid[idx[a]][idx[b]] += 1

    # 선물지수 = 준 개수 - 받은 개수
    score = [sum(grid[i]) - sum(row[i] for row in grid) for i in range(n)]
    next_gift = [0] * n

    # 두 사람 비교
    for i in range(n):
        for j in range(i+1, n):
            if grid[i][j] > grid[j][i]:
                next_gift[i] += 1
            elif grid[i][j] < grid[j][i]:
                next_gift[j] += 1
            else:
                if score[i] > score[j]:
                    next_gift[i] += 1
                elif score[j] > score[i]:
                    next_gift[j] += 1

    return max(next_gift)
