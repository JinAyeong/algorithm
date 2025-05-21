'''
- 블록 타입 : 1*1, 1*2, 2*1
- 초록 보드
    - 열 고정된 상태로 아래방향으로 블록 떨어짐
    - 가로 줄이 모두 차면 제거, 위에 있는 블록은 아래로 이동
    - 0, 1번 행 중 블록이 있으면, 가장 아래 행부터 차례로 한 줄씩 삭제, 비원진 만큼 위에서 밀어내림
- 파란 보드
    - 행 고정된 상태로 오른쪽방향으로 블록 떨어짐
    - 세로 줄이 모두 차면 제거, 왼쪽에 있는 블록은 오른쪽으로 이동
    - 0, 1번 열 중 블록이 있으면, 가장 오른쪽 열부터 차례로 한 줄씩 삭제, 비워진 만큼 왼쪽에서 밀어내림
'''

N = int(input())

blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
score = 0


# 블록 떨어뜨리기
def drop_block(t, x, y):

    # 초록 보드
    if t == 1:
        r = 0
        while r+1 < 6 and green[r+1][y] == 0:
            r += 1
        green[r][y] = 1
    elif t == 2:
        r = 0
        while r+1 < 6 and green[r+1][y] == 0 and green[r+1][y+1] == 0:
            r += 1
        green[r][y] = 1
        green[r][y+1] = 1
    elif t == 3:
        r = 0
        while r+2 < 6 and green[r+2][y] == 0:
            r += 1
        green[r][y] = 1
        green[r+1][y] = 1

    # 파란 보드
    if t == 1:
        c = 0
        while c+1 < 6 and blue[x][c+1] == 0:
            c += 1
        blue[x][c] = 1
    elif t == 2:
        c = 0
        while c+2 < 6 and blue[x][c+2] == 0:
            c += 1
        blue[x][c] = 1
        blue[x][c+1] = 1
    elif t == 3:
        c = 0
        while c+1 < 6 and blue[x][c+1] == 0 and blue[x+1][c+1] == 0:
            c += 1
        blue[x][c] = 1
        blue[x+1][c] = 1


# 줄 제거 및 점수 계산
def check_line():
    global score

    # 초록
    while True:
        found = False
        for i in range(5, 1, -1):
            if all(green[i]):
                score += 1
                found = True
                for r in range(i, 0, -1):
                    green[r] = green[r - 1][:]
                green[0] = [0] * 4
                break
        if not found:
            break

    # 파랑
    while True:
        found = False
        for j in range(5, 1, -1):
            if all(blue[r][j] for r in range(4)):
                score += 1
                found = True
                for c in range(j, 0, -1):
                    for r in range(4):
                        blue[r][c] = blue[r][c - 1]
                for r in range(4):
                    blue[r][0] = 0
                break
        if not found:
            break


# 연한 칸 확인
def check_light():

    # 초록
    cnt = 0
    for i in [0, 1]:
        if any(green[i]):
            cnt += 1
    for _ in range(cnt):
        green.pop()
        green.insert(0, [0]*4)

    # 파랑
    cnt = 0
    for j in [0, 1]:
        if any(blue[i][j] for i in range(4)):
            cnt += 1
    for _ in range(cnt):
        for r in range(4):
            blue[r].pop()
            blue[r].insert(0, 0)


for _ in range(N):
    t, x, y = map(int, input().split())
    drop_block(t, x, y)
    check_line()
    check_light()

print(score)
print(sum(sum(line) for line in green) + sum(sum(line) for line in blue))