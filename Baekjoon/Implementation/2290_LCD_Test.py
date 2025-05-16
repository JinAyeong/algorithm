s, n = input().split()
s = int(s)

# 숫자 디지털 판
num_pos = {
    '0': [0, 1, 2, 4, 5, 6],
    '1': [2, 5],
    '2': [0, 2, 3, 4, 6],
    '3': [0, 2, 3, 5, 6],
    '4': [1, 2, 3, 5],
    '5': [0, 1, 3, 5, 6],
    '6': [0, 1, 3, 4, 5, 6],
    '7': [0, 2, 5],
    '8': [0, 1, 2, 3, 4, 5, 6],
    '9': [0, 1, 2, 3, 5, 6],
}

rows = 2 * s + 3
cols = (s + 2 + 1) * len(n) - 1
result = [[" " for _ in range(cols)] for _ in range(rows)]

def lcd(start_col, num):
    pos = num_pos[num]

    # 0번 위치
    if 0 in pos:
        for i in range(1, s + 1):
            result[0][start_col + i] = "-"

    # 1번 위치
    if 1 in pos:
        for i in range(1, s + 1):
            result[i][start_col] = "|"

    # 2번 위치
    if 2 in pos:
        for i in range(1, s + 1):
            result[i][start_col + s + 1] = "|"

    # 3번 위치
    if 3 in pos:
        for i in range(1, s + 1):
            result[s + 1][start_col + i] = "-"

    # 4번 위치
    if 4 in pos:
        for i in range(s + 2, 2 * s + 2):
            result[i][start_col] = "|"

    # 5번 위치
    if 5 in pos:
        for i in range(s + 2, 2 * s + 2):
            result[i][start_col + s + 1] = "|"

    # 6번 위치
    if 6 in pos:
        for i in range(1, s + 1):
            result[2 * s + 2][start_col + i] = "-"

for idx, num in enumerate(n):
    start_col = idx * (s + 3)
    lcd(start_col, num)

for line in result:
    print("".join(line))
