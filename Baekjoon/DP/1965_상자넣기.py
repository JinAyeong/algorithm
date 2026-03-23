'''
상자 순서대로 넣을 수 있는 최대 수 구하기
'''

N = int(input())
boxes = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(N):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))