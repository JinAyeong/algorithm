'''
i번 파이어볼의 위치: (r, c), 질량 m, 방향 d, 속력 s

이동명령 시작
1. 자신의 방향 d로 속력 s칸 만큼 이동 (같은 칸에 여러개의 파이어볼 가능)
2. 두개의 파이어볼이 있는 칸
    2-1. 하나로 합쳐짐
    2-2. 4개의 파이어볼로 나누어짐
    2-3. 질량 : 합쳐진 파이어볼 질량의 합 / 5
    2-4. 속력 : 합쳐진 파이어볼 속력의 합 / 합쳐진 파이어볼의 수
    2-5. 합쳐지는 파이어볼의 방향이 모두 홀수 or 짝수 - 방향 0, 2, 4, 6 / 아니면 1, 3, 5, 7
    2-6. 질량이 0인 파이어볼 : 소멸되어 없어짐
3. 이동명령 K번 후, 남아있는 파이어볼 질량의 합 구하기
'''

import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
mp = [[deque([]) for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    mp[r-1][c-1].append((m, s, d))

def move(mp):

    move_mp = [[deque([]) for _ in range(N)] for _ in range(N)]
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            cur_pos = mp[i][j]

            while cur_pos:
                m, s, d = cur_pos.popleft()
                ni, nj = (i + dir[d][0] * s) % N, (j + dir[d][1] * s) % N
                move_mp[ni][nj].append((m, s, d))

    new_mp = [[deque([]) for _ in range(N)] for _ in range(N)]
    # 질량 합치기
    for i in range(N):
        for j in range(N):
            cur_pos = move_mp[i][j]

            if len(move_mp[i][j]) == 0:
                continue

            if len(move_mp[i][j]) == 1:
                new_mp[i][j] = move_mp[i][j]

            else:
                nm = sum(inform[0] for inform in cur_pos) // 5
                if nm == 0:
                    continue

                ns = sum(inform[1] for inform in cur_pos) // len(cur_pos)

                all_even = all(inform[2] % 2 == 0 for inform in cur_pos)
                all_odd = all(inform[2] % 2 == 1 for inform in cur_pos)
                nd_list = [0, 2, 4, 6] if all_even or all_odd else [1, 3, 5, 7]

                for nd in nd_list:
                    new_mp[i][j].append((nm, ns, nd))

    return new_mp

for _ in range(K):
    mp = move(mp)

answer = 0

for i in range(N):
    for j in range(N):
        for m, s, d in mp[i][j]:
            answer += m

print(answer)