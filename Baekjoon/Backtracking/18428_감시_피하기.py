# 세개의 장애물 설치
# 설치 후에 선생님의 시야에 닿는지 확인
# 닿으면 바로 return NO

N = int(input())
school = [list(map(str, input().split())) for _ in range(N)]
teachers = []

# 선생님 찾기
for a in range(N):
    for b in range(N):

        if school[a][b] == 'T':
            teachers.append((a, b))

# 장애물 설치하기
def obstacle(cnt):

    if cnt == 3:
        # 감시에 닿는지 확인
        if avoid(school):
            print('YES')
            exit(0)
        return

    for i in range(N):
        for j in range(N):
            if school[i][j] == 'X':
                school[i][j] = 'O'
                obstacle(cnt + 1)
                school[i][j] = 'X'

# 감시 피하기
def avoid(arr):

    for teacher in teachers:
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = teacher
            while True:
                nr += dr
                nc += dc
                # 범위를 벗어나면 중단
                if not (0 <= nr < N and 0 <= nc < N):
                    break
                # 장애물을 만나면 중단
                if arr[nr][nc] == 'O':
                    break
                # 학생을 만나면 실패
                if arr[nr][nc] == 'S':
                    return False
    return True


obstacle(0)
print('NO')