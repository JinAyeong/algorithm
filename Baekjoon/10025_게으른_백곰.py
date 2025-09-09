'''
1. 총 N개의 얼음 양동이
2. xi 좌표위에 gi씩의 얼음
3. 자리를 잡으면 좌우로 K만큼 떨어진 양동이까지 잡기 가능
'''

N, K = map(int, input().split())
mp = [0] * 1000001

for _ in range(N):
    x, g = map(int, input().split())
    mp[x] = g

cur_sum = sum(mp[:min(2 * K + 1, 1000001)])
answer = cur_sum

left, right = 0, 2 * K

while right <= 20:

    print(left, right, cur_sum)

    cur_sum -= mp[left]
    cur_sum += mp[right]
    
    left += 1
    right += 1

    answer = max(cur_sum, answer)

print(answer)