'''
s: 양, w: 늑대
s 상하좌우에 w가 있으면 0출력
상하좌우에 D 심기
'''

R, C = map(int, input().split())
mp = [list(input()) for _ in range(R)]

def solve():

    for i in range(R):
        for j in range(C):
            if mp[i][j] == 'W':
                # 상하좌우에 양 있는지 확인
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        if mp[ni][nj] == '.':
                            mp[ni][nj] = 'D'
                        elif mp[ni][nj] == 'S':
                            return 0

    return 1

answer = solve()
print(answer)

if answer:
    for line in mp:
        print("".join(line))