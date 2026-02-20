'''
조건
- 체스판 N * N 크기, 말의 개수 K개
- 하나의 말 위에 다른 말 올릴 수 있다.
- 체스판 한 칸 : 흰색 0 , 빨간색 1, 파란색 2 중 하나
- 말 : 1~K번까지의 번호, 이동방향 오왼위아1234 로 이동
- 1턴 : 1번말부터 K번 말까지 순서대로 이동, 이동시에 위에 올려진 말도 함께 이동
- 턴이 진행되던 중, 말이 4개 이상 쌓이면 종료
- 이동하려는 칸이 흰색 : 그 칸으로 extend
- 이동하려는 칸이 빨간색 : 이동할 말 전부 뒤집어서 extend
- 이동하려는 칸이 파란색 : 이동 방향을 반대로 하고 한 칸 이동 (방향을 바꾼 후에도 파란색일경우에는 무시)
- 체스판을 벗어나는 경우 : 파란색과 똑같이 행동
- 말이 4개 이상 쌓이면 종료
'''

'''
풀이
- mp 위에 말 리스트로 쌒기 (extend)
- 각 말의 위치 따로 저장 -> 매 턴마다 순서대로 움직이기
    1. 말의 위치와 방향 확인
    2. 그 말의 mp 에서 인덱스 확인
    3. 그대로 뜯어서 옮기기
'''

N, K = map(int, input().split())
mp_color = [list(map(int, input().split())) for _ in range(N)]
mp = [[[] for _ in range(N)] for _ in range(N)]
marker = []

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 오, 왼, 위, 아래
reverse_dir = {0:1, 1:0, 2:3, 3:2}

for k in range(K):
    r, c, d = map(lambda x: int(x)-1, input().split())
    mp[r][c].append(k)
    marker.append([r, c, d])

# 말 자르기
def cut_stack(num, r, c):
    idx = mp[r][c].index(num)
    moving = mp[r][c][idx:]
    mp[r][c] = mp[r][c][:idx]
    return moving

# 위치 갱신
def update_position(moving, nr, nc):
    for m in moving:
        marker[m][0] = nr
        marker[m][1] = nc

# 말 쌓기
def place_stack(moving, nr, nc, color):
    if color == 0:
        mp[nr][nc].extend(moving)
    else:
        mp[nr][nc].extend(reversed(moving))

    update_position(moving, nr, nc)

turn = 0

while turn <= 1000:
    turn += 1

    for num in range(K):
        r, c, d = marker[num]

        moving = cut_stack(num, r, c)

        nr = r + dir[d][0]
        nc = c + dir[d][1]

        # 파란색 or 범위 밖
        if not (0 <= nr < N and 0 <= nc < N) or mp_color[nr][nc] == 2:
            d = reverse_dir[d]
            marker[num][2] = d

            nr = r + dir[d][0]
            nc = c + dir[d][1]

            # 또 파란색이면 이동 취소
            if not (0 <= nr < N and 0 <= nc < N) or mp_color[nr][nc] == 2:
                mp[r][c].extend(moving)
                continue

        place_stack(moving, nr, nc, mp_color[nr][nc])

        if len(mp[nr][nc]) >= 4:
            print(turn)
            exit(0)

print(-1)