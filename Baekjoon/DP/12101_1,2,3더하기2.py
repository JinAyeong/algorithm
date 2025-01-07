n, k = map(int, input().split())

dp = dict()

dp[0] = ['']
dp[1] = ['1']
dp[2] = ['1+1', '2']
dp[3] = ['1+1+1', '1+2', '2+1', '3']

for i in range(4, n+1):
    dp[i] = []

    for j in dp[i-1]:
        dp[i].append(j + '+1')

    for j in dp[i-2]:
        dp[i].append(j + '+2')

    for j in dp[i-3]:
        dp[i].append(j + '+3')

try:
    dp[n].sort()
    print(dp[n][k-1])
except:
    print(-1)

# n, k = map(int, input().split())
#
# dp = [[] for i in range(12)]
# dp[0] = ['']
# dp[1] = ['1']
# dp[2] = ['1+1', '2']
# dp[3] = ['1+1+1', '1+2', '2+1', '3']
#
# for i in range(4, n+1):
#
#     for j in range(len(dp[i-1])):
#         dp[i].append(dp[i-1][j] + '+1')
#
#     for j in range(len(dp[i-2])):
#         dp[i].append(dp[i-2][j] + '+2')
#
#     for j in range(len(dp[i-3])):
#         dp[i].append(dp[i-3][j] + '+3')
#
# try:
#     dp[n].sort()
#     print(dp[n][k-1])
# except:
#     print(-1)