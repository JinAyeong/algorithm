N = int(input())
board = [list(input()) for _ in range(N)]
heart = (0, 0)
leg_start = (0, 0)
length = [0, 0, 0, 0, 0]


# 머리 찾기
found = False

for a in range(N):

    if found:
        break

    for b in range(N):
        if board[a][b] == '*':
            heart = (a+1, b)
            found = True
            break


# 왼쪽 팔 길이
for i in range(heart[1] - 1, -1, -1):
    if board[heart[0]][i] == '*':
        length[0] += 1
    else:
        break

# 오른쪽 팔 길이
for i in range(heart[1] + 1, N):
    if board[heart[0]][i] == '*':
        length[1] += 1
    else:
        break

# 허리 길이
for i in range(heart[0] + 1, N):
    if board[i][heart[1]] == '*':
        length[2] += 1
    else:
        leg_start = (i, heart[1])
        break

# 왼쪽 다리 길이
for i in range(leg_start[0], N):
    if board[i][leg_start[1]-1] == '*':
        length[3] += 1
    else:
        break

# 오른쪽 다리 길이
for i in range(leg_start[0], N):
    if board[i][leg_start[1]+1] == '*':
        length[4] += 1
    else:
        break

# 인덱스 조정
heart = map(lambda x: x+1, heart)

print(*heart)
print(*length)