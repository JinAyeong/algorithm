'''
1. 총 N개의 얼음 양동이
2. xi 좌표위에 gi씩의 얼음
3. 자리를 잡으면 좌우로 K만큼 떨어진 양동이까지 잡기 가능
'''

N, K = map(int, input().split())
mp = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())
    mp[x] = g

window_size = 2 * K + 1
cur_sum = sum(mp[:window_size])
answer = cur_sum

left, right = 0, window_size - 1

while right + 1 < len(mp):
    cur_sum -= mp[left]
    left += 1
    right += 1
    cur_sum += mp[right]
    answer = max(answer, cur_sum)

print(answer)

