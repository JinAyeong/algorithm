# 공 모으는 방법 : 경계선에 어느 색깔의 공이든 옮겨놓으면 알아서 분류됨

N = int(input())
balls = list(input())

# 위에서 아래 탐색
cur = balls[-1]
line = False
start = 0
right_R = 0
right_B = 0

for i in range(N-1, -1, -1):

    # 경계선이 안나타났다면 나올때까지 경계선 찾기
    if balls[i] != cur:
        line = True
        start = i
        break

if line:
    for j in range(start, -1, -1):

        # 경계선 찾았으면 공 색깔별로 세어주기
        if balls[j] == 'B':
            right_B += 1
        elif balls[j] == 'R':
            right_R += 1


# 아래서 위 탐색
cur = balls[0]
line = False
start = 0
left_R = 0
left_B = 0

for i in range(N):

    # 경계선이 안나타났다면 나올때까지 경계선 찾기
    if balls[i] != cur:
        line = True
        start = i
        break

if line:
    for j in range(start, N):

        # 경계선 찾았으면 공 색깔별로 세어주기
        if balls[j] == 'B':
            left_B += 1
        elif balls[j] == 'R':
            left_R += 1

# print(left_R, left_B, right_B, right_R)
print(min(left_R, left_B, right_B, right_R))