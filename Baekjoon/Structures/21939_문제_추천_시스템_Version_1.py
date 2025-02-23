# recommend x : x == 1 : 문제 추천 리스트에서 가장 어려운 문제의 번호 출력 (여러개라면 제일 큰 수)
# recommend x : x == -1 : 문제 추천 리스트에서 가장 쉬운 문제의 번호 출력 (여러개라면 제일 작은 수)
# add P L : 난이도가 L인 문제번호 P 추가
# solved P : 문제번호 P 제거
from heapq import heappush, heappop

N = int(input())
max_q = []
min_q = []
exist = {}

for _ in range(N):
    num, level = map(int, input().split())
    heappush(min_q, (level, num))
    heappush(max_q, (-level, -num))
    exist[num] = level

M = int(input())

for _ in range(M):
    order, *numbers = list(input().split())
    numbers = list(map(int, numbers))

    if order == 'recommend':
        if numbers[0] == -1:

            while min_q:
                cur_l, cur_n = min_q[0]

                if cur_n in exist and exist[cur_n] == cur_l:
                    print(cur_n)
                    break
                else:
                    heappop(min_q)


        elif numbers[0] == 1:

            while max_q:
                cur_l, cur_n = max_q[0]

                if -cur_n in exist and exist[-cur_n] == -cur_l:
                    print(-cur_n)
                    break
                else:
                    heappop(max_q)

    elif order == 'add':

        heappush(min_q, (numbers[1], numbers[0]))
        heappush(max_q, (-numbers[1], -numbers[0]))
        exist[numbers[0]] = numbers[1]

    elif order == 'solved':
        exist.pop(numbers[0])

