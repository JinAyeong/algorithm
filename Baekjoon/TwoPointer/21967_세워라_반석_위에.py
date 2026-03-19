'''
구간 안의 최댓값, 최솟값의 차이가 2인 구간중 가장 긴 구간 찾기
-> 슬라이딩 윈도우
'''

from collections import deque

N = int(input())
perms = list(map(int, input().split()))

min_q = deque()
max_q = deque()

left = 0
answer = 0

for right in range(N):
    while min_q and perms[min_q[-1]] > perms[right]:
        min_q.pop()
    min_q.append(right)

    while max_q and perms[max_q[-1]] < perms[right]:
        max_q.pop()
    max_q.append(right)

    while perms[max_q[0]] - perms[min_q[0]] > 2:
        left += 1

        if min_q[0] < left:
            min_q.popleft()
        if max_q[0] < left:
            max_q.popleft()

    answer = max(answer, right - left + 1)

print(answer)