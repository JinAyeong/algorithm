'''
K개의 랜선을 N개의 같은 길이의 랜선으로 만들기
이때, 최대 랜선의 길이
'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

low = 1
high = max(arr)
answer = 0

while low <= high:

    mid = (low + high) // 2
    cnt = 0

    for line in arr:
        cnt += line // mid

    if cnt >= N:
        low = mid + 1
        answer = mid

    else:
        high = mid - 1

print(answer)