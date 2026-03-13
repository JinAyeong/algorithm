'''
4x4 공간에 물고기 한마리 존재
각 물고기는 8가지 방향, 1이상 16 이하의 자연수 가짐
'''

from copy import deepcopy

arr = [list(map(int, input().split())) for _ in range(4)]
mp = [[] for _ in range(4)] # (물고기 번호, 물고기 방향)
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fishes = [(0, 0, 0) for _ in range(17)] # (r, c, d)
shark = (0, 0, -1)

'''
초기 설정
'''

for i in range(4):
    for j in range(4):
        num, d = arr[i][j*2], arr[i][j*2 + 1] - 1

        if (i, j) == (0, 0):
            shark = (0, 0, d)
            fishes[num] = (-1, -1, -1)
            mp[i].append((-1, -1))
        else:
            fishes[num] = (i, j, d)
            mp[i].append((num, d))


'''
물고기 이동
1. 번호가 작은 물고기부터
2. 한 칸 이동
3. 빈 칸, 다른 물고기가 있는 칸 이동 가능
4. 상어가 있는 칸 이동 불가능
5. 이동할 수 있는 칸이 나올 떄까지 45도 반시계 회전
6. 이동할 수 없으면 이동하지 않음
7. 다른 물고기가 있는 칸으로 이동할 떄는 서로 위치 바꿈
'''

def move_fish(cur_mp, cur_fishes):
    
    for num in range(1, 17):
        r, c, d = cur_fishes[num]

        if (r, c, d) == (-1, -1, -1):
            continue

        for i in range(8):
            nd = (d + i) % 8
            dr, dc = dir[nd]
            nr, nc = r+dr, c+dc

            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue

            if cur_mp[nr][nc][0] == -1:
                continue

            target, td = cur_mp[nr][nc]

            cur_mp[r][c] = (target, td)
            cur_mp[nr][nc] = (num, nd)

            cur_fishes[num] = (nr, nc, nd)

            if target > 0:
                cur_fishes[target] = (r, c, td)

            break

    return cur_mp, cur_fishes


'''
상어 이동
1. 한번에 여러 칸 이동
2. 물고기가 있는 칸으로 이동 : 물고기 먹고 그물고기의 방향 따름
3. 물고기가 없는 칸으로 이동 불가능
4. 이동할 수 없으면 집으로
5. 상어는 (0, 0)에서 시작
상어가 먹을 수 있는 물고기 번호 합의 최댓값 구하기
'''

def move_shark(size, cur_mp, cur_fishes, cur_shark):

    r, c, d = cur_shark

    nr, nc = r + dir[d][0] * size, c + dir[d][1] * size

    if 0 <= nr < 4 and 0 <= nc < 4 and cur_mp[nr][nc][0] > 0:
        fish_num, fish_dir = cur_mp[nr][nc]

        cur_mp[r][c] = (0, 0)
        cur_mp[nr][nc] = (-1, -1)
        cur_fishes[fish_num] = (-1, -1, -1)
        shark = (nr, nc, fish_dir)

        return True, cur_mp, cur_fishes, shark, fish_num
    else:
        return False, cur_mp, cur_fishes, cur_shark, 0


'''
사이클 반복
'''
answer = 0

def dfs(mp, fishes, shark, cur_sum):
    global answer

    mp = deepcopy(mp)
    fishes = deepcopy(fishes)

    mp, fishes = move_fish(mp, fishes)

    moved = False

    for s in range(1,4):

        temp_mp = deepcopy(mp)
        temp_fishes = deepcopy(fishes)

        can_move, next_mp, next_fishes, next_shark, eat = move_shark(s, temp_mp, temp_fishes, shark)

        if can_move:
            moved = True
            dfs(next_mp, next_fishes, next_shark, cur_sum + eat)

    if not moved:
        answer = max(answer, cur_sum)

dfs(mp, fishes, shark, arr[0][0])

print(answer)