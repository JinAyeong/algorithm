# 윈도우 defaultdict으로 관리
# python 34924KB, 836ms

from collections import defaultdict

# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

sushi_count = defaultdict(int)

# 초기 deque에서 dict로 변경
for i in range(k):
    sushi_count[sushi[i]] += 1
sushi_count[c] += 1  # 쿠폰 초밥 포함


max_num = len(sushi_count)


for i in range(N):

    # 맨 앞 초밥 제거
    left = sushi[i]
    sushi_count[left] -= 1
    if sushi_count[left] == 0:
        del sushi_count[left]

    # 맨 뒤 초밥 추가
    right = sushi[(i + k) % N]
    sushi_count[right] += 1

    max_num = max(max_num, len(sushi_count))

print(max_num)

# --------------------------------------------
# 윈도우 deque으로 관리
# python 35316KB, 3496ms
# pypy 178300KB, 2200ms

from collections import deque

# 연속해서 초밥 k개 먹으면 쿠폰번호 초밥 하나 공짜
# result = 초밥 가짓수의 최댓값

# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

arr = deque(sushi[:k])
max_num = 0


for i in range(N):

    cur_arr = set(arr) # 현재 연속한 초밥
    num = len(cur_arr) # 초밥 수

    if c in cur_arr:
        max_num = max(max_num, num)
    else:
        max_num = max(max_num, num + 1)

    # 다음 초밥 비교 준비
    arr.popleft()
    arr.append(sushi[(i+k) % N])

print(max_num)